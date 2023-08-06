import React from 'react';
import { WidgetModel } from '@jupyter-widgets/base';
import { useModelState, WidgetModelContext } from './hooks/widget-model';

interface WidgetProps {
  model: WidgetModel;
}

function ReactWidget(props: WidgetProps) {
  const [value, setValue] = useModelState('value');
  const [xlim] = useModelState('xlim');
  const [ylim] = useModelState('ylim');
  const [width] = useModelState('width');
  const [height] = useModelState('height');

  const x = value[0];
  const y = value[1];
  const xmin = xlim[0];
  const xmax = xlim[1];
  const ymin = ylim[0];
  const ymax = ylim[1];

  console.log({ x, xmin, xmax, y, ymin, ymax });

  const [isPointerDown, setIsPointerDown] = React.useState(false);
  const svgRef = React.useRef<SVGSVGElement>(null);

  const setXYFromEvent = (e: React.PointerEvent) => {
    const target = svgRef.current;
    if (target) {
      const rect = target.getBoundingClientRect();
      const newX =
        xmin +
        ((e.clientX - rect.left) / (rect.right - rect.left)) * (xmax - xmin);
      const newY =
        ymin +
        ((e.clientY - rect.bottom) / (rect.top - rect.bottom)) * (ymax - ymin);
      setValue([newX, newY]);
    }
  };

  return (
    <div className="Widget">
      <svg
        ref={svgRef}
        width={width}
        height={height}
        onPointerDown={(e) => {
          setIsPointerDown(true);
          setXYFromEvent(e);
        }}
        onPointerUp={(e) => {
          setIsPointerDown(false);
        }}
        onPointerMove={(e) => {
          if (isPointerDown) {
            setXYFromEvent(e);
          }
        }}
      >
        <rect width={width} height={height} fill="blue" />
        <circle
          cx={((x - xmin) / (xmax - xmin)) * width}
          cy={((ymax - y) / (ymax - ymin)) * height}
          r={0.05 * Math.min(width, height)}
          fill="red"
        />
      </svg>
      <br />
      {`x: ${x}`}
      <br />
      {`y: ${y}`}
    </div>
  );
}

function withModelContext(Component: (props: WidgetProps) => JSX.Element) {
  return (props: WidgetProps) => (
    <WidgetModelContext.Provider value={props.model}>
      <Component {...props} />
    </WidgetModelContext.Provider>
  );
}

export default withModelContext(ReactWidget);
