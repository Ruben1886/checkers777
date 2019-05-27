function ajax(object){
    $.ajax({
        url: '/game', /*w ktorej sciezce routowania to odpieramy*/
        type: 'POST',
        dataType:'text', /*oczekiwane dane*/
        contentType: 'application/json', /*dane do wysylki*/
        data:JSON.stringify(object),
        success: function()
        {
            $('#p_communicates_head').load('/game' + ' #p_communicates_head').fadeOut('fast').fadeIn('fast');
            $('#p_communicates').load('/game' + ' #p_communicates').fadeOut('fast').fadeIn('fast');
            $('#gB').load('/game' + ' #gB').fadeTo("fast", 1).fadeIn('slow');

            console.log('succes'); /*mozna tu tez renderowac*/
        },
        error: function(err, s , exception)
        {
            console.log(exception);
        }
    });
}

const moves = [];

function get_coords(a,b){

    moves.push(a,b);

    if(moves.length > 3){
        ajax( {start_row:moves[0], start_column:moves[1], end_row:moves[2], end_column:moves[3]});
        moves.length = 0; /*clearing the array*/
    }
}

function copy_to_clipboard() {
    var copyText = document.getElementById("link");
    copyText.select();
    document.execCommand("copy");
}