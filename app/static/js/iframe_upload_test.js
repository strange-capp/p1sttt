window.onload = function() {
    // подвязываем переменные к элементам
    var $send_btn = document.getElementById('send'),
        $input = document.getElementById('file'),
        $iframe = document.getElementById('iframe23'),
        form = document.createElement('form'); // здесь создается динамическая форма
    document.body.appendChild(form);
    // настраиваем форму
    form.target = $iframe.name;
    form.action = 'make_gif/save_files';
    form.method = 'POST';
    form.enctype = 'multipart/form-data';
    // вешаем обработчик событий на кнопку отправки
    $send_btn.addEventListener('click', function(e) {
        e.preventDefault();
        // сохраняем соседние и родительские элементы, чтобы потом можно было вернуть файловый инпут
        var sibling = $input.nextSibling,
            parent = $input.parentNode;
        // переносим файловый инпут в форму
        form.appendChild($input);
        // отправляем форму
        form.submit();
        // очищаем инпут
        $input.value = '';
        // возвращаем инпут на прежнее место
        if(sibling)
            parent.insertBefore($input, sibling);
        else
            parent.appendChild($input);
    });
    // вешаем обработчик события onload на iframe
    $iframe.addEventListener('load', function(e) {
        // получаем содержимое с которым можно делать все что угодно
        var server_data = $iframe.contentWindow.document.body.innerHTML;
    });
}