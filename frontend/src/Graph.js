import React, { useRef, useLayoutEffect } from 'react';
import * as d3 from 'd3';

const Graph = ({ pointArray }) => {
    console.log('Hi! This is the graph component! The received point array is: ', pointArray);
    // local points: [40.4, [30, 40, 45, 50, 37]]

    const svgRef = useRef();
    useLayoutEffect(() => {
        if (!pointArray || !pointArray.points || pointArray.points.length !== 2) {
            return;
        }

        // Destructure the points array
        const [averagePoints, specificScores] = pointArray.points;

        // setting up the svg container
        const w = 500;
        const h = 300;
        const svg = d3.select(svgRef.current)
        .attr('width', w)
        .attr('height', h)
        .style('overflow', 'visible')
        .style('margin-top', '65px')
        .style('color', 'white');

        // setting the scaling
        const xScale = d3.scaleBand()
        .domain(specificScores.map((val, i) => i))
        .range([0, w])
        .padding(0.4);

        const yScale = d3.scaleLinear()
        .domain([0, d3.max(specificScores)])  // Adjust domain based on the specificScores data
        .range([h, 0]);

        // setting the axes
        const xAxis = d3.axisBottom(xScale)
        .ticks(specificScores.length);

        const yAxis = d3.axisLeft(yScale)
        .ticks(specificScores.length);

        svg.append('g')
        .call(xAxis)
        .attr('transform', `translate(0, ${h})`);

        svg.append('g')
        .call(yAxis);

        // setting the svg data
        svg.selectAll('.bar')
        .data(specificScores)
        .join('rect')
        .attr('x', (v, i) => xScale(i))
        .attr('y', val => yScale(val))
        .attr('width', xScale.bandwidth())
        .attr('height', val => h - yScale(val))
        .attr('fill', 'white');
    }, [pointArray]);

    return (
        <div className='graph-div'>
            <svg ref={svgRef}></svg>
        </div>
    );
};

export default Graph;
