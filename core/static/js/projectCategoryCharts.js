google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    const numPolicyStatusByProject = async (projectId) => {
        try {
            let data = [];
            if (projectId == '0') {
                var policiesData = [
                    ['Políticas', 'Estados'],
                    ['Seleccione un proyecto', 32],
                    ['Borrador', 0],
                    ['Descontinuado', 0]
                ];
                data = policiesData;
            } else {
                const response = await fetch('/categoriesList/' + projectId + '/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                const dataJson = await response.json();
                data = dataJson;

            }
            return data;
    
        } catch (error) {
            // Mostrar el mensaje de error en la interfaz de usuario
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = 'Se produjo un error al cargar los proyectos.';
            
            // Registrar el error en la consola del navegador para fines de depuración
            //console.error(error);
            var policiesData = [
                ['Políticas', 'Estados'],
                ['Seleccione un proyecto', 32],
                ['Borrador', 0],
                ['Descontinuado', 0]
            ];
            return policiesData;
        }
    };

    var data = google.visualization.arrayToDataTable([
        ['Políticas', 'Estados'],
        ['Aprobado', 0.0000001],
        ['Borrador', 0.0000001],
        ['Descontinuado', 0.0000001]
    ]);

    var data2 = google.visualization.arrayToDataTable([
        ['Controles', 'Estados'],
        ['Aprobado', 0.0000001],
        ['Borrador', 0.0000001],
        ['Descontinuado', 0.0000001]
    ]);

    var options = {
        title: 'Políticas',
        is3D: false,
        legend: 'none'
    };

    var options2 = {
        title: 'Controles',
        is3D: false,
        legend: 'none'
    };

    for (var i = 0; i < 11; i++) {
        var chart = new google.visualization.PieChart(document.getElementById('pieChartPolicy'+(i+1)));
        chart.draw(data, options);

        var chart2 = new google.visualization.PieChart(document.getElementById('pieChartControl'+(i+1)));
        chart2.draw(data2, options2);
    }
    
    // Event listener to detect changes in the selected project
    document.getElementById('projectSelect').addEventListener('change', function () {
        // Get the selected project ID
        var selectedProjectId = this.value;

        numPolicyStatusByProject(selectedProjectId).then((values) => {


            try{
                charts = [];
                dataTables = [];
                if (selectedProjectId == '0') {
                    for (var i = 0; i < 11; i++) {
                        var chart = new google.visualization.PieChart(document.getElementById('pieChartPolicy'+(i+1)));
                        chart.draw(data, options);
                
                        var chart2 = new google.visualization.PieChart(document.getElementById('pieChartControl'+(i+1)));
                        chart2.draw(data2, options2);
                    }
                }else{
                    for (var i = 0; i < values['policies'].length; i++) {
                        console.log(data[i]);
                        dataTables[i] = google.visualization.arrayToDataTable(values['policies'][i]);
                        charts[i] = new google.visualization.PieChart(document.getElementById('pieChartPolicy'+(i+1)));
                        charts[i].draw(dataTables[i], options);
    
                        dataTables[i] = google.visualization.arrayToDataTable(values['controls'][i]);
                        charts[i] = new google.visualization.PieChart(document.getElementById('pieChartControl'+(i+1)));
                        charts[i].draw(dataTables[i], options2);
    
                    }

                }
                
                
            }
            catch(error){
                console.log(error);
                for (var i = 0; i < 11; i++) {
                    var chart = new google.visualization.PieChart(document.getElementById('pieChartPolicy'+(i+1)));
                    chart.draw(data, options);
            
                    var chart2 = new google.visualization.PieChart(document.getElementById('pieChartControl'+(i+1)));
                    chart2.draw(data2, options2);
                }
            }

            

        });

    });
}



