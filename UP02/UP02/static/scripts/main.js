document.addEventListener('DOMContentLoaded', function() {
    addColumn(20);
});

function addColumn(n) {
    // Находим таблицу
    let table = document.getElementById('input-table');

    // Проходим по каждой строке в таблице и добавляем новую ячейку
    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < n; j++) {
            let cell = document.createElement('td');
            let input = document.createElement('input');
            input.type = 'text';
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

    if (tableLenght() != 3) {
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
                });
            };
            
            reader.readAsText(file);
        }
    };
    
    input.click();
}

function processData(t) {
    const buttons = document.querySelectorAll('.tabs-container button');
    buttons.forEach(button => {
        if (button.id === `btn${t}`) {
            if (!button.classList.contains('active')) {
                button.classList.add('active');
            }
        } else {
            button.classList.remove('active');
        }
    });

    // Сбор данных из таблицы в двумерный массив
    var table = document.getElementById('input-table');
    var data = [];
    var file = '';
    var tag = '';

    for (var i = 0; i < table.rows.length; i++) {
        var rowData = [];
        for (var j = 1; j < table.rows[i].cells.length; j++) {
            rowData.push(table.rows[i].cells[j].querySelector('input[type="text"]').value);
        }
        data.push(rowData);
    }

    switch (t) {
        case '12': { file = 'approximation.html'; tag = 'container-1234'; break; }
        case '3': { file = 'comparison.html'; tag = 'container-1234'; break; }
        case '4': { file = 'analyzing.html'; tag = 'container-1234'; break; }
    }

    // Отправка данных на сервер (можно использовать AJAX запрос)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', `/load-html/${file}/${tag}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const myDiv = document.getElementById('container-1234');
                // myDiv.innerHTML = ''; // очищаем содержимое контейнера
                myDiv.outerHTML = xhr.responseText; // устанавливаем новый фрагмент разметки
            } else {
                console.error('Ошибка при запросе на сервер');
            }
        }
    };
    xhr.send(JSON.stringify(data));

    return false; // Чтобы форма не отправляла данные по умолчанию
}
