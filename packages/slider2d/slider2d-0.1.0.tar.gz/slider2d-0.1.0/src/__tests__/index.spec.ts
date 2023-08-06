// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// Add any needed widget imports here (or from controls)
// import {} from '@jupyter-widgets/base';

import { createTestModel } from './utils';

import { Slider2DModel } from '..';

describe('Slider2D', () => {
  describe('Slider2DModel', () => {
    it('should be createable', () => {
      const model = createTestModel(Slider2DModel);
      expect(model).toBeInstanceOf(Slider2DModel);
      expect(model.get('value')).toEqual([0, 0]);
    });

    it('should be createable with a value', () => {
      const state = { value: [0.5, 0.5] };
      const model = createTestModel(Slider2DModel, state);
      expect(model).toBeInstanceOf(Slider2DModel);
      expect(model.get('value')).toEqual([0.5, 0.5]);
    });
  });
});
