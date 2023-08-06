# -*- coding:utf-8 -*-
# @Time     :2023/2/1 3:22 下午
# @Author   :CHNJX
# @File     :swaggergen_api.py
# @Desc     :将swagger转换成api-object
import os
import sys

sys.path.append(os.path.dirname(sys.path[0]))

import codecs
from os.path import dirname, exists
from jinja2 import FileSystemLoader, Environment
import click

from swaggergen_api.loader_swagger import load_swagger

group = click.Group()


@click.command('generate')
@click.option('-s', '--swagger-doc',
              required=True, help='Swagger doc file.')
@click.option('-d', '--api-dir',
              required=True, help='api save dir.')
def generate(swagger_doc, api_dir):
    swagger_data = load_swagger(swagger_doc)
    _generate_template_path(swagger_data['paths'])
    tag_path_dict = _generate_template_data(swagger_data)
    template = _get_template()
    for tag, paths in tag_path_dict.items():
        content = _get_api_content(template, tag=tag, paths=paths)
        file_path = os.path.join(api_dir, tag + '.py')
        _write(content, file_path)


group.add_command(generate)


def _write(content, file_path):
    dir_ = dirname(file_path)
    if not exists(dir_):
        os.makedirs(dir_)
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(content)


def _get_api_content(template, **kwargs):
    return template.render(**kwargs)


def _get_template():
    loader = FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 'templates'))
    env = Environment(loader=loader)
    return env.get_template('api.tpl')


def _get_method_attribute(value) -> str:
    attribute = ''
    if value.get('get'):
        attribute = 'get'
    elif value.get('post'):
        attribute = 'post'
    elif value.get('put'):
        attribute = 'put'
    elif value.get('delete'):
        attribute = 'delete'
    return attribute


def _transformation_parameters(parameters) -> list:
    return [param for param in parameters if
            param['name'] != 'raw' and param['name'] != 'root' and param['in'] != 'header']


def _transformation_json(parameters) -> list:
    json_list = []
    for param in parameters:
        if param.get('schema') and param['schema'].get('properties'):
            for key_name in param['schema']['properties'].keys():
                json_list.append(key_name)
    return json_list


def _transformation_params_list(params, json_params: list) -> list:
    params_name_list: list = [param['name'] for param in params]
    params_name_list.extend(json_params)
    return params_name_list


def _generate_url(path) -> str:
    path_name_list = path.split('/')
    if 'id' in path_name_list[-1]:
        path_name_list.pop(-1)
    return '/'.join(path_name_list)


def _generate_name(path) -> str:
    path_name_list = path.split('/')
    return path_name_list[-2].split('?')[0] if 'id' in path_name_list[-1] else \
        path_name_list[-1].split('?')[0]


def _transformation_file(json_params) -> list:
    return [param for param in json_params if 'file' in param]


def _generate_template_path(swagger_paths):
    for path, value in swagger_paths.items():
        method_attribute = _get_method_attribute(value)
        value['method'] = method_attribute
        value['tag'] = value[method_attribute]['tags'][0]
        value['desc'] = value[method_attribute]['summary']
        parameters = value[method_attribute]['parameters']
        value['parameters'] = _transformation_parameters(parameters)
        value['json'] = _transformation_json(parameters)
        value['files'] = _transformation_file(value['json'])
        value['params_list'] = _transformation_params_list(value['parameters'], value['json'])
        value['url'] = _generate_url(path)
        value['name'] = _generate_name(path)


def _generate_template_data(swagger_data) -> dict:
    tag_path_dict = {}
    for tag in swagger_data['tags']:
        tag_name: str = tag['name']
        tag_name = tag_name.replace('/', '-', -1)
        tag_path_list = {name: path for name, path in swagger_data['paths'].items() if
                         path['tag'].replace('/', '-', -1) == tag_name}
        tag_path_dict[tag_name] = tag_path_list
    return tag_path_dict


if __name__ == '__main__':

    print(sys.path)
    group.main()
