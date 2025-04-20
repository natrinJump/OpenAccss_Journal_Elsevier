// Main results
$('.result-table > data').each(function(){
  var title = $(this).data('journal');
  var abbr = $(this).data('abbr');
  var percentage = (Math.floor(+$(this).data('percentage') * 1000) / 10).toFixed(1);

  $(this).parent().append(`
    <li class="result-item">
      <span class="result-journal">${title} <span class="result-abbr">${abbr}</span></span>
      <span class="result-percentage">${percentage}%</span>
    </li>
  `);
});

var abbrMap = {
  'subj_area_model': 'Subject Area Model',
  'mult': 'General',
  'agri': 'Agricultural and Biological Sciences',
  'arts': 'Arts and Humanities',
  'bioc': 'Biochemistry, Genetics and Molecular Biology',
  'busi': 'Business, Management and Accounting',
  'ceng': 'Chemical Engineering',
  'chem': 'Chemistry',
  'comp': 'Computer Science',
  'deci': 'Decision Sciences',
  'eart': 'Earth and Planetary Sciences',
  'econ': 'Economics, Econometrics and Finance',
  'ener': 'Energy',
  'engi': 'Engineering',
  'envi': 'Environmental Science',
  'immu': 'Immunology and Microbiology',
  'mate': 'Materials Science',
  'math': 'Mathematics',
  'medi': 'Medicine',
  'neur': 'Neuroscience',
  'nurs': 'Nursing',
  'phar': 'Pharmacology, Toxicology and Pharmaceutics',
  'phys': 'Physics and Astronomy',
  'psyc': 'Psychology',
  'soci': 'Social Sciences',
  'vete': 'Veterinary',
  'heal': 'Health Professions'
};

var labels = [];
var dataRaw = [];
$('#pieChartData > data').each(function(){
  labels.push(abbrMap[$(this).data('subj')]);
  dataRaw.push((Math.floor(+$(this).data('acc') * 1000)/10).toFixed(1));
});

// Pie chart
const ctx = $('#pieChart')[0];
const data = {
  labels: labels,
  datasets: [{
    label: 'Influence on result %',
    data: dataRaw
  }]
};
const chart = new Chart(ctx, {
  type: 'pie',
  data: data,
  options: {
    responsive: true,
    aspectRatio: 1.75|1,
    plugins: {
      legend: {position: 'right'}
    }
  }
});