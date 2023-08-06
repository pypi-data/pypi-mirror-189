// Copyright (c) nicolvisser
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';
import ReactWidget from "./ReactWidget"
import React from 'react';
import ReactDOM from 'react-dom';

import { MODULE_NAME, MODULE_VERSION } from './version';

// Import the CSS
import '../css/widget.css';

// Your widget state goes here. Make sure to update the corresponding
// Python state in example.py
const defaultModelProperties = {
    value: [0.0, 0.0],
    xlim: [0.0, 1.0],
    ylim: [0.0, 1.0],
    width: 100,
    height: 100,
  };

export type WidgetModelState = typeof defaultModelProperties

export class Slider2DModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: Slider2DModel.model_name,
      _model_module: Slider2DModel.model_module,
      _model_module_version: Slider2DModel.model_module_version,
      _view_name: Slider2DModel.view_name,
      _view_module: Slider2DModel.view_module,
      _view_module_version: Slider2DModel.view_module_version,
      ...defaultModelProperties
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'Slider2DModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'Slider2DView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class Slider2DView extends DOMWidgetView {
  render() {
    this.el.classList.add('custom-widget');

    const component = React.createElement(ReactWidget, {
      model: this.model,
    });
    ReactDOM.render(component, this.el);
  }
}
