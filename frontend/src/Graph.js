import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const Graph = ({ pointArray }) => {
  const svgRef = useRef(null);

  useEffect(() => {
    // D3.js code for rendering the graph
    const svg = d3.select(svgRef.current);

    // Example: Creating circles based on the pointArray
    svg
      .selectAll('circle')
      .data(pointArray)
      .enter()
      .append('circle')
      .attr('cx', (d) => d.x)
      .attr('cy', (d) => d.y)
      .attr('r', 5)
      .attr('fill', 'blue');

    // You can customize this code based on your specific use case

  }, [pointArray]);

  console.log('Hi! This is the graph component! The received point array is: ', pointArray);

  return (
    <div>
      <svg ref={svgRef}></svg>
    </div>
  );
};

export default Graph;