$(document).ready(function () {

    $('#analytics').click(function () {
        $(this).remove();
        /*
        $.getJSON('http://ec2-18-221-63-105.us-east-2.compute.amazonaws.com/macrocomb5/macrocomb5/public/js/data.json',function(dataset){
        getBubbles(dataset);
        });
        */

        $.getJSON(BASE_URL + '/viz',function(dataset){
        getBubbles(dataset);
        });

    });

    function getBubbles(dataset) {

        var diameter = 600;
        var color = d3.scaleOrdinal(['#abebc6',
            '#82e0aa',
            '#58d68d',
            '#2ecc71',
            '#28b463',
            '#239b56']);
        //var color = d3.scaleOrdinal(d3.schemeYlGn);        

        var bubble = d3.pack(dataset)
            .size([diameter, diameter])
            .padding(1.5);

        var svg = d3.selectAll("div").select("svg")
            .attr("width", diameter)
            .attr("height", diameter)
            .attr("class", "bubble");

        var nodes = d3.hierarchy(dataset)
            .sum(function (d) { return d.Count * 10 + 50; });

        var node = svg.selectAll(".node")
            .data(bubble(nodes).descendants())
            .enter()
            .filter(function (d) {
                return !d.children
            })
            .append("g")
            .attr("class", "node")
            .attr("transform", function (d) {
                return "translate(" + d.x + "," + d.y + ")";
            });

        node.append("title")
            .text(function (d) {
                return d.Name + ": " + d.Count;
            });

        node.append("circle")
            .attr("r", function (d) {
                return d.r;
            })
            .style("fill", function (d, i) {
                return color(i);
            });

        node.append("text")
            .attr("dy", ".2em")
            .style("text-anchor", "middle")
            .text(function (d) {
                return d.data.Count;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", function (d) {
                return d.r / 5;
            })
            .attr("fill", "white");

        d3.select(self.frameElement)
            .style("height", diameter + "px");

    }



});
