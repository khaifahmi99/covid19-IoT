// get the data
const proxyurl = "https://cors-anywhere.herokuapp.com/";
let urlG = 'https://8vli4zwpec.execute-api.ap-southeast-2.amazonaws.com/dev/api/chart?triggerType=Glove'
let urlC = 'https://8vli4zwpec.execute-api.ap-southeast-2.amazonaws.com/dev/api/chart?triggerType=Cough'
let urlF = 'https://8vli4zwpec.execute-api.ap-southeast-2.amazonaws.com/dev/api/chart?triggerType=Fall'


let dataG = fetch(proxyurl + urlG).then(d => d.json()).then(dataG => {
    let projectData = dataG.map(item => {
        dataset = dataG;
        console.log(dataG);
        console.table(dataG);
        console.log(d3.selectAll(dataG).size());
        //lineChart(dataset);
        return item.Timestamp;

    });

    function tabulate(dataG, columns) {
        var table = d3.select('body').append('table')
            .attr("style", "margin-left: 200px")
            .style("border-collapse", "collapse")
            .style("border", "2px black solid")
        var thead = table.append('thead')
        var tbody = table.append('tbody');

        // append the header row
        thead.append('tr')
            .selectAll('th')
            .data(columns).enter()
            .append('th')
            .text(function(column) { return column; });

        // create a row for each object in the data
        var rows = tbody.selectAll('tr')
            .data(dataG)
            .enter()
            .append('tr');

        // create a cell in each row for each column
        var cells = rows.selectAll('td')
            .data(function(row) {
                return columns.map(function(column) {
                    return { column: column, value: row[column] };
                });
            })
            .enter()
            .append('td')
            .text(function(d) { return d.value; });

        return table;
    }

    // render the table(s)
    tabulate(dataG, ['Confidence', 'Timestamp', 'TriggerType', 'Id']); // 4 column table

});

let dataC = fetch(proxyurl + urlC).then(d => d.json()).then(dataC => {
    let projectData = dataC.map(item => {
        dataset = dataC;
        console.log(dataC);
        console.log(d3.selectAll(dataC).size());
        //lineChart(dataset);
        return item.Timestamp;

    });

    function tabulate(dataC, columns) {
        var table = d3.select('body').append('table')
            .attr("style", "margin-left: 200px")
            .style("border-collapse", "collapse")
            .style("border", "2px black solid")
        var thead = table.append('thead')
        var tbody = table.append('tbody');

        // append the header row
        thead.append('tr')
            .selectAll('th')
            .data(columns).enter()
            .append('th')
            .text(function(column) { return column; });

        // create a row for each object in the data
        var rows = tbody.selectAll('tr')
            .data(dataC)
            .enter()
            .append('tr');

        // create a cell in each row for each column
        var cells = rows.selectAll('td')
            .data(function(row) {
                return columns.map(function(column) {
                    return { column: column, value: row[column] };
                });
            })
            .enter()
            .append('td')
            .text(function(d) { return d.value; });

        return table;
    }

    // render the table(s)
    tabulate(dataC, ['Confidence', 'Timestamp', 'TriggerType', 'Id']); // 4 column table


});

let dataF = fetch(proxyurl + urlF).then(d => d.json()).then(dataF => {
    let projectData = dataF.map(item => {
        dataset = dataF;
        console.log(dataF);
        console.log(d3.selectAll(dataF).size());

        //lineChart(dataset);
        return item.Timestamp;

    });

    function tabulate(dataF, columns) {
        var table = d3.select('body').append('table')
            .attr("style", "margin-left: 200px")
            .style("border-collapse", "collapse")
            .style("border", "2px black solid")
        var thead = table.append('thead')
        var tbody = table.append('tbody');

        // append the header row
        thead.append('tr')
            .selectAll('th')
            .data(columns).enter()
            .append('th')
            .text(function(column) { return column; });

        // create a row for each object in the data
        var rows = tbody.selectAll('tr')
            .data(dataF)
            .enter()
            .append('tr');

        // create a cell in each row for each column
        var cells = rows.selectAll('td')
            .data(function(row) {
                return columns.map(function(column) {
                    return { column: column, value: row[column] };
                });
            })
            .enter()
            .append('td')
            .text(function(d) { return d.value; });

        return table;
    }

    // render the table(s)
    tabulate(dataF, ['Confidence', 'Timestamp', 'TriggerType', 'Id']); // 4 column table
});