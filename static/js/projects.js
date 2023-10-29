let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [],
    pageLength: 10,
    destroy: true
};

const initDataTable = async() => {
    if(dataTableIsInitialized){
        dataTable.destroy();
    }
    await projectsList();

    dataTable=$('#dataTable-projects').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const projectsList = async() => {
    try{
        const response = await fetch('/projectsList/', {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        console.log(data);

        let content = ``;
        data.projects.forEach((project, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td><a href="/projectRead/${project.id}/">${project.name}</a></td>   
                    <td>${project.startDate}</td>
                    <td>${project.endDate}</td>
                </tr>
            `;
        });
        document.getElementById('dataBody-projects').innerHTML = content;
    }catch(error){
        alert(error);
    }
};

window.addEventListener('load', async() => {
    await initDataTable();
});