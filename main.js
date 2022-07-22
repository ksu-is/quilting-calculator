function calculate(width, length, numFabrics, fabricWidth, silkyFabricWidth) {
  var ret = {};

  // Constants
  var BACK_SQUARE_SIDE = 4.5;
  var SEAM_WIDTH = 0.25;
  var FRONT_SQUARE_SIDE = 6;
  var PUFF_SIZE = BACK_SQUARE_SIDE - 2 * SEAM_WIDTH;
  var RUFFLE_WIDTH = 8;
  var RUFFLE_MULTIPLICATION_FACTOR = 1.85;

  // Defaults
  ret.fabricWidth = fabricWidth || 44;
  ret.silkyFabricWidth = silkyFabricWidth || 44;
  ret.numFabrics = numFabrics || 4;

  // Useful functions
  function amountOfFabricForSquares(numSquares, squareSize) {
    var numInRow = Math.floor(ret.fabricWidth / squareSize);
    var numColumns = Math.ceil(numSquares / numInRow);
    return numColumns * squareSize;
  }

  // Round up for x and y to next multiple of 4
  ret.width = Math.ceil(width / PUFF_SIZE) * 4;
  ret.length = Math.ceil(length / PUFF_SIZE) * 4;

  // Number of puffs
  ret.numPuffs = ret.width * ret.length / 16;

  // Amount of back material
  ret.backFabricAmount = amountOfFabricForSquares(ret.numPuffs, BACK_SQUARE_SIDE);

  // Amount of front material for each color
  ret.numPuffsPerFabric = Math.ceil(ret.numPuffs / ret.numFabrics);
  ret.frontFabricAmount = amountOfFabricForSquares(ret.numPuffsPerFabric, FRONT_SQUARE_SIDE);

  // Amount of silky fabric
  var perimeter = 2 * width + 2 * length;
  var lengthOfSilkyFabric = Math.ceil(perimeter * RUFFLE_MULTIPLICATION_FACTOR);
  ret.numStripsSilky = Math.ceil(lengthOfSilkyFabric / ret.silkyFabricWidth);
  ret.silkyFabricAmount = ret.numStripsSilky * RUFFLE_WIDTH;

  return ret;
}

$(function() {
  $("#form").submit(function(event) {
    var $inputs = $('#form :input');
    var values = {};
    $inputs.each(function() {
      values[this.name] = $(this).val();
    });

    var result = calculate(values.width, values.length, values.numFabrics, values.fabricWidth, values.silkyFabricWidth);
    console.log(result);
  
    var output = _.template($('#outputTemplate').html(), result);
    console.log(output);
    $('#output').html(output);

    event.preventDefault();
  });
});


