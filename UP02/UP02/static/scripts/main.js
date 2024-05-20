document.addEventListener('DOMContentLoaded', function() {
    addColumn(20);
});

function showContent(tabName) {
    const selectedContent = document.getElementById(`container-1234`);

    if (selectedContent.style.display != 'block') {
        selectedContent.style.display = 'block'
    }
    
    if (selectedContent) {
        switch (tabName) {
            case '12': { loadHTML('approximation.html', 'container-1234'); break; }
            case '3': { loadHTML('comparison.html', 'container-1234'); break; }
            case '4': { loadHTML('analyzing.html', 'container-1234'); break; }
        }
    }
}

function handleButtonClick(id) {
    const buttons = document.querySelectorAll('.tabs-container button');
    buttons.forEach(button => {
        if (button.id === `btn${id}`) {
            if (!button.classList.contains('active')) {
                button.classList.add('active');
                showContent(id);
            }                
        } else {
            button.classList.remove('active');
        }
    });
    
}

function addColumn(n) {
    // Находим таблицу
    let table = document.getElementById('input-table');

    // Проходим по каждой строке в таблице и добавляем новую ячейку
    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < n; j++) {
            let cell = document.createElement('td');
            let input = document.createElement('input');
            input.type = 'text';
            // input.type = 'number';
            input.value = '0';
            input.addEventListener('click', function() {
                this.select();
            });
            cell.appendChild(input);
            table.rows[i].appendChild(cell);
        }
    }
}

function removeColumn(n) {
    // Находим таблицу
    let table = document.getElementById('input-table');

    if (tableLenght() != 2) {
        // Проходим по каждой строке в таблице и удаляем последнюю ячейку
        for (let i = 0; i < table.rows.length; i++) {
            for (let j = 0; j < n; j++) {
                table.rows[i].deleteCell(-1);
            }
        }
    }
}

// Функция для удаления символов перевода строки (\r) из массива
function cleanArray(array) {
    return array.map(row => row.map(cell => cell.toString().replace(/\r/g, '')));
}

function csvToArray (csv) {
    rows = csv.split("\n");

    return rows.map(function (row) {
    	return row.split(",");
    });
};

function tableLenght() {
    // Находим таблицу
    let table = document.getElementById('input-table');

    const headerRow = table.querySelector('tr');
    const headerCells = Array.from(headerRow.querySelectorAll('td'));
    const columnCount = headerCells.length;

    return columnCount;
}

function loadFromCSV() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.csv';
    var csvData = "";

    input.onchange = function(e) {
        const file = e.target.files[0];
        
        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                csvData = e.target.result;
                console.log('Данные из CSV файла: \n', csvData);

                var array = cleanArray(csvToArray(csvData));

                console.log('Преобразованный массив: ', array);

                // Находим таблицу
                let table = document.getElementById('input-table');

                const columnCount = tableLenght();

                removeColumn(columnCount);
                
                // Проходим по каждой строке массива
                array.forEach((rowData, rowIndex) => {
                    // Проходим по каждому элементу текущей строки массива
                    rowData.forEach((cellData) => {
                        // Создаем новую ячейку в строке
                        const cell = document.createElement('td');
                        const input = document.createElement('input');
                        input.type = 'text';
                        input.value = cellData;
                        cell.appendChild(input);
                        table.rows[rowIndex].appendChild(cell);
                    });

                    // Добавляем дополнительные пустые ячейки, если необходимо
                    //const emptyColumns = Math.max(0, array[0].length - rowData.length);
                    //if (emptyColumns > 0) {
                    //    for (let i = 0; i < emptyColumns; i++) {
                    //        const cell = document.createElement('td');
                    //        const input = document.createElement('input');
                    //        input.type = 'number';
                    //        input.value = '0';
                    //        cell.appendChild(input);
                    //        row.appendChild(cell);
                    //    }
                    //}
                });
            };
            
            reader.readAsText(file);
        }
    };
    
    input.click();
}

function loadHTML(file, tag) {
    fetch(`/load-html/${file}/${tag}`)
        .then(response => response.text())
        .then(data => {
            const myDiv = document.getElementById(tag);
            // myDiv.innerHTML = ''; // очищаем содержимое контейнера
            myDiv.outerHTML = data; // устанавливаем новый фрагмент разметки
        })
        .catch(error => {
            console.log('An error occurred:', error);
        });
}