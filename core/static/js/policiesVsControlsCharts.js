google.charts.load('current', { 'packages': ['bar'] });
google.charts.setOnLoadCallback(drawStuff);

function drawStuff() {

    

    const policiesVsControls = async () => {
        try {
            let data = [];

            const response = await fetch('/vanillaPoliciesList/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const dataJson = await response.json();
            data = dataJson['policies'];

            data.unshift(['Políticas', 'Número de Controles']);

            return data;

        } catch (error) {
            // Mostrar el mensaje de error en la interfaz de usuario
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = 'Se produjo un error al cargar los proyectos.';

            // Registrar el error en la consola del navegador para fines de depuración
            console.error(error);
            var policiesData = [
                ['Políticas', 'Estados'],
                ['Seleccione un proyecto', 32],
                ['Borrador', 0],
                ['Descontinuado', 0]
            ];
            return policiesData;
        }
    };


    policiesVsControls().then((values) => {
        //console.log(values)
        var data = new google.visualization.arrayToDataTable(values);

        var options = {
            width: 800,
            legend: { position: 'none' },
            chart: {
                title: 'Número de Controles por Política',
                subtitle: 'Por favor, hacer Clic en la gráfica para ver el número de controles de cada política'
            },
            axes: {
                x: {
                    0: { side: 'bottom', label: 'Controles'} // Top x-axis.
                },
                y: {
                    0: { side: 'top', label: 'Políticas' } // Top y-axis.
                }
            },
            bar: { groupWidth: "100%" },
            bars: 'horizontal', // Required for Material Bar.
        };

        var chart = new google.charts.Bar(document.getElementById('top_x_div'));
        // Convert the Classic options to Material options.
        chart.draw(data, google.charts.Bar.convertOptions(options));
    })


};