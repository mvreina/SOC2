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
                const response = await fetch('/policiesList/' + projectId + '/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                const dataJson = await response.json();
                data = dataJson['policies'];

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
        ['Seleccione un proyecto', 32],
        ['Borrador', 0],
        ['Descontinuado', 0]
    ]);

    var options = {
        title: 'Políticas del proyecto',
        is3D: true
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);

    // Event listener to detect changes in the selected project
    document.getElementById('projectSelect').addEventListener('change', function () {
        // Get the selected project ID
        var selectedProjectId = this.value;

        numPolicyStatusByProject(selectedProjectId).then((data) => {
            //console.log(data);
            var policiesData = data;
            var chart = new google.visualization.PieChart(document.getElementById('piechart'));
            chart.draw(google.visualization.arrayToDataTable(policiesData), options);

            const tableBody = document.getElementById('dataBodyPolicies');
            tableBody.innerHTML = ''; // Limpia el contenido existente

            if (selectedProjectId == '0') {
                const initTable = [['Aprobado', 0],
                    ['Descontinuado', 0],
                    ['Borrador', 0],
                    ['Total', 0],
                ];
                initTable.forEach((item, index) => {

                    const row = tableBody.insertRow();
                    const cellIndex = row.insertCell(0);
                    const cellName = row.insertCell(1);
                    cellIndex.textContent = item[0];
                    cellName.textContent = item[1];
                    if(index == 3) {
                        cellIndex.classList.add('bold-text'); // Add a class for styling
                        cellName.classList.add('bold-text'); // Add a class for styling
                    }
                    
                });
                
            } else {
                let total = 0;
                policiesData.forEach((item, index) => {
                    if(index > 0) {
                        const row = tableBody.insertRow();
                        const cellIndex = row.insertCell(0);
                        const cellName = row.insertCell(1);
                        cellIndex.textContent = item[0];
                        cellName.textContent = item[1];
                        total += item[1];
                    }
                });
                const row = tableBody.insertRow();
                const cellIndex = row.insertCell(0);
                const cellName = row.insertCell(1);
                cellIndex.textContent = 'Total';
                cellName.textContent = total;
                cellIndex.classList.add('bold-text'); // Add a class for styling
                cellName.classList.add('bold-text'); // Add a class for styling
            }
        });

    });
        
}



