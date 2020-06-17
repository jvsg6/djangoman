$(document).ready(function(){
    $("#WindOroFormBtn").click(function(){
       var serializedData = $("#WindOroForm").serialize();
       console.log(serializedData);
       $.ajax({
            url: '/edit/29/',
            data: serializedData,
            type: 'post',
        success: function(response) {
            $("#windOroPhaseListTable > tbody").append('<tr>'+
            '<td>' + response.newWindOroPhase.meteoPhaseStart +'</td>'+
            '<td>' + response.newWindOroPhase.windConst +'</td>'+
            '<td>' + response.newWindOroPhase.precipitationsRate +'</td>'+
            '<td>' + response.newWindOroPhase.precipitationType +'</td>'+
            '<td>' + response.newWindOroPhase.stab +'</td>'+
            '<td>' + response.newWindOroPhase.roughness +'</td>'+
            '<td><button type="button" class="btn btn-danger"><i class="fa fa-trash mr-2"></button></td>'+
            '</tr>'
                )
        }
       })
    });
});


