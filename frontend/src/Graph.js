import React, { useRef, useEffect, useState } from 'react';
import * as d3 from 'd3';

const Graph = ({ graphArray }) => {
    const svgRef = useRef();
    const tooltipRef = useRef(null);
    const [tooltipData, setTooltipData] = useState(null);

    useEffect(() => {
        const handleMouseMove = (event) => {
            if (tooltipData) {
                const tooltipElement = d3.select(tooltipRef.current);
                const offset = 10; // Adjust this value to set the distance from the cursor
                const leftPos = event.pageX + offset;
                const topPos = event.pageY;

                tooltipElement
                    .style('left', `${leftPos}px`)
                    .style('top', `${topPos}px`);
            }
        };

        document.addEventListener('mousemove', handleMouseMove);

        return () => {
            document.removeEventListener('mousemove', handleMouseMove);
        };
    }, [tooltipData]);

    useEffect(() => {
        if (!graphArray || !graphArray.points || graphArray.points.length !== 2) {
            return;
        }

        const [averagePoints, specificScores] = graphArray.points;
        const columnWidth = 100;
        const padding = 0.4;
        const dynamicWidth = specificScores.length * (columnWidth + padding);

        const h = 250;
        const svg = d3.select(svgRef.current)
            .attr('width', dynamicWidth)
            .attr('height', h)
            .style('margin-top', '40px')
            .style('margin-left', '-15%')
            .style('margin-bottom', '-5%')
            .style('overflow', 'visible');

        const xScale = d3.scaleBand()
            .domain(specificScores.map((val, i) => i))
            .range([0, dynamicWidth])
            .padding(padding);

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(specificScores)])
            .range([h, 0]);

        const xAxis = d3.axisBottom(xScale)
            .ticks(specificScores.length);

        const yAxis = d3.axisLeft(yScale)
            .ticks(specificScores.length);

        svg.selectAll('*').remove();

        svg.append('g')
            .call(xAxis)
            .attr('transform', `translate(0, ${h})`);

        svg.append('g')
            .call(yAxis);

        const bars = svg.selectAll('.bar')
            .data(specificScores)
            .join('g')
            .attr('class', 'bar-group');

        bars.append('rect')
            .attr('x', (v, i) => xScale(i))
            .attr('y', v => yScale(v))
            .attr('width', xScale.bandwidth())
            .attr('height', v => h - yScale(v))
            .style('transition', 'transform 0.2s ease-in-out')
            .style('cursor', 'pointer')
            .attr('rx', 5)
            .attr('fill', v => (v < averagePoints) ? 'red' : '#00BF63')
            .on('mouseover', (event, d, i) => {
                d3.select(event.target)
                    .style('transform', 'scale(1.01)')
                const overUnder = (d < averagePoints) ? 'UNDER' : 'OVER';
                const tooltipText = `${overUnder} ${averagePoints}`;
                setTooltipData({
                    text: tooltipText,
                    x: event.pageX,
                    y: event.pageY,
                });
            })
            .on('mouseout', (event) => {
                d3.select(event.target)
                    .style('transform', 'scale(1.0)')

                setTooltipData(null);
            });

        bars.append('text')
            .text(v => v)
            .attr('x', (v, i) => xScale(i) + xScale.bandwidth() / 2)
            .attr('y', v => yScale(v) - 5)
            .attr('text-anchor', 'middle')
            .style('fill', 'white');
    }, [graphArray]);

    useEffect(() => {
        if (tooltipData) {
            const tooltipElement = d3.select(tooltipRef.current);
            const tooltipWidth = 40; // Adjust this value based on the tooltip content

            tooltipElement
                .style('fill', 'black')
                .style('background-color', 'white')
                .style('width', `${tooltipWidth}px`)
                .style('padding', '5px')
                .text(tooltipData.text)
                .style('display', 'block')
                .style('position', 'absolute')
                .style('float', 'left')
                .style('border-radius', '5px');
        } else {
            d3.select(tooltipRef.current).style('display', 'none');
        }
    }, [tooltipData]);

    return (
        <div className='graph-div'>
            <svg ref={svgRef}></svg>
            <div className="tooltip" ref={tooltipRef}></div>
        </div>
    );
};

export default Graph;