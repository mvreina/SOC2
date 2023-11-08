let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await projectsList();

    dataTable = $('#dataTable-projects').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const projectsList = async () => {
    try {
        const response = await fetch('/projectsList/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        //console.log(data);

        const tableBody = document.getElementById('dataBody-projects');
        tableBody.innerHTML = ''; // Limpia el contenido existente

        data.projects.forEach((project, index) => {
            const row = tableBody.insertRow();
            const cellIndex = row.insertCell(0);
            const cellName = row.insertCell(1);
            const cellStartDate = row.insertCell(2);
            const cellEndDate = row.insertCell(3);

            cellIndex.textContent = index + 1;
            const projectNameLink = document.createElement('a');
            projectNameLink.href = `/projectRead/${project.id}/`;
            projectNameLink.textContent = decodeHtmlEntities(project.name);
            cellName.appendChild(projectNameLink);
            cellStartDate.textContent = project.startDate;
            cellEndDate.textContent = project.endDate;
        });
    } catch (error) {
        // Mostrar el mensaje de error en la interfaz de usuario
        const errorMessage = document.getElementById('error-message');
        errorMessage.textContent = 'Se produjo un error al cargar los proyectos.';
        
        // Registrar el error en la consola del navegador para fines de depuración
        //console.error(error);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
});

function decodeHtmlEntities(html) {
    return html
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'")
        .replace(/&nbsp;/g, ' ')
        .replace(/&amp;/g, '&')
        .replace(/&#32;/g, " ")
        .replace(/&#47/,"/")
        .replace(/&#63;/,"?"); // Replace &nbsp; with a space
}