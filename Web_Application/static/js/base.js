$(".chosen-select").chosen({
  no_results_text: "No results matching:"
});

var abstract_input = 'textarea[name="abstract"]';
var subj_area_input = 'select[name="subj-area"]+.chosen-container';
var subj_area_choices = 'select[name="subj-area"]+.chosen-container > .chosen-choices > li.search-choice';

$("form input[type='submit']").click(function(e){
  var valid = true;

  // Abstract container
  if ($(abstract_input)[0].value == '') {
    $(abstract_input).addClass('invalid');
    valid = false;
  } else {
    $(abstract_input).removeClass('invalid');
  }

  // Subject-areas container
  if (!$(subj_area_choices).length) {
    $(subj_area_input).addClass('invalid');
    valid = false;
  } else {
    $(subj_area_input).removeClass('invalid');
    
  }

  if (!valid) {
    e.preventDefault();
  } else {
    $('.loader').css('display','block');
  }
});