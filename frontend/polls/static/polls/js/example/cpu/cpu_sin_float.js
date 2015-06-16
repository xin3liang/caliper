
$(function () {
	var test = document.getElementById("cpu_tst").value;  
    
    var sin_float_dic = getJson(test, 'sincore_float')
    var columns = getHoriColumn(sin_float_dic);
    var data = getHoriData(sin_float_dic, columns);
       
    // initialize grid
    var options = {emptyRow: true, sortable: false};
	var grid = $(".sensei-grid:eq(5)").grid(data, columns, options);

    draw_grid(grid);

    // api examples
    var $row = grid.getRowByIndex(5);
    console.group("data api examples");
    console.log("grid.getRowDataByIndex(0):", grid.getRowDataByIndex(0));
    console.log("grid.getRowData($row):", grid.getRowData($row));
    console.log("grid.getGridData():", grid.getGridData());
    console.groupEnd();

    window.grid = grid;
});
