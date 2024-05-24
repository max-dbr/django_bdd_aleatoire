
   $(document).ready(function() {
    $('.datatable').DataTable({
        "lengthMenu": [ [10, 25, 50, 100, -1], [10, 25, 50, 100, "Tout"] ],
        "pageLength": -1,
        "language": {
            "sLengthMenu": "Afficher _MENU_ entrées par page",
            "sSearch": "Rechercher :",
            "sInfo": "Affichage de _START_ à _END_ sur _TOTAL_ entrées",
            "sInfoEmpty": "Affichage de 0 à 0 sur 0 entrées",
            "sInfoFiltered": "(filtré sur _MAX_ total entrées)",
            "oPaginate": {
                "sNext": "Suivant",
                "sPrevious": "Précédent"
            },
            "info": ""  // Supprime complètement l'affichage du nombre total d'entrées
        }
    });
});
