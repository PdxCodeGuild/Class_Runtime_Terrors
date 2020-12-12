$(document).ready(function() {
    console.log('loaded!');
})
let item = $('#input_field');
let output = $('#output');
let add = $('#add');
let remove = $('#delete');
let todo = $('#todo');
let done = $('#done');

$('#add').on('click',function(){
    let $li = "<li>" + item.val() + "</li>";
    todo.append($li);
    $('#input_field').val('');
})

$('#todo').on('click', 'li', function(){
    let $li = "<li>" + ('todo li') + "</li>";
    done.append(('<li>' + $(this).text() + '</li>'));
    $(this).remove();
    
})
$('#done li').css("text-decoration", "line-through");



