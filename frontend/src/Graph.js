import React, { useRef, useLayoutEffect } from 'react';
import * as d3 from 'd3';

const Graph = ({ pointArray }) => {
    const svgRef = useRef();
    useLayoutEffect(() => {
        console.log('Hi! This is the graph component! The received point array is: ', pointArray.points);
        if (!pointArray || !pointArray.points || pointArray.points.length !== 2) {
            return;
        }
        
        const [averagePoints, specificScores] = pointArray.points;
        // Calculate the dynamic width based on the number of columns
        const columnWidth = 100; // Width of each column
        const padding = 0.4; // Padding between columns
        const dynamicWidth = specificScores.length * (columnWidth + padding);

        // setting up the svg container
        const h = 250;
        const svg = d3.select(svgRef.current)
            .attr('width', dynamicWidth)
            .attr('height', h)
            .style('margin-top', '30px')
            .style('margin-left', '-15%')
            .style('color', 'black');

        // setting the scaling
        const xScale = d3.scaleBand()
            .domain(specificScores.map((val, i) => i))
            .range([0, dynamicWidth])
            .padding(padding);

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(specificScores)])
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
            .attr('y', v => yScale(v))
            .attr('width', xScale.bandwidth())
            .attr('height', v => h - yScale(v))
            .attr('fill', v => (v < averagePoints) ? 'red' : '#00BF63');

    }, [pointArray]);

    return (
        <div className='graph-div'>
            <svg ref={svgRef}></svg>
        </div>
    );
};

export default Graph;