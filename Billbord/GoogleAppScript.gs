function createForm() {
  const document = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = document.getSheets()[0];
  const range = sheet.getDataRange();
  const values = range.getValues();
  const artistsName = values.slice(1);
  
  var form = FormApp.create('Billboard');
  form.addGridItem()
      .setTitle('Rate artists')
      .setRows(artistsName)
      .setColumns([1, 2, 3, 4, 5]);
  Logger.log('Published URL: ' + form.getPublishedUrl());
  Logger.log('Editor URL: ' + form.getEditUrl());
}




function dataSummary() {
  const document = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = document.getSheets()[0];
  const range = sheet.getDataRange();
  const values = range.getValues();
  const artists = values.slice(1);

  var form = FormApp.openById('1N9n1rRUwsok0XGIM7CI2fbhMZ8BzGtDQzNwNutX2wGk');
  var formResponses = form.getResponses();
  var respondentsNum = formResponses.length;

  var sums = [], i = 0;
  while (i < artists.length) {
    sums.push(0);
    i++;
  }
  for (const element of formResponses) {
    var itemResponses = element.getItemResponses();
    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      var votesOfArtists = itemResponse.getResponse();
      for (var k = 0; k < votesOfArtists.length; k++) {
        sums[k] += parseInt(votesOfArtists[k]);
      }
    }
  }
  for (var i = 0; i < artists.length; i++) {
    var cell = sheet.getRange("B" + (i+2)); 
    cell.setValue(sums[i] / respondentsNum);
  }
  }









