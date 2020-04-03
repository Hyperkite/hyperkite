'use strict';
jQuery.fn.exists = function(){ return this.length > 0; }


function updateCreateStudyForm() {
    length = $('#subforms-container .subform').length;
    for(var i=0; i<length; i++) {
        var parameter_type = document.querySelector('input[name="create_study_parameters-'+i+'-parameter_type"]:checked').value;

        /* Update button images */
        var n_types = 5;
        for(var j=0; j<n_types; j++) {
            $('#create_study_parameters-'+i+'-parameter_type-btn-'+j).hide();
        }

        if (parameter_type == 'randint') {
            $('#create_study_parameters-'+i+'-parameter_type-btn-0').show();
        } else if (parameter_type == 'uniform') {
            $('#create_study_parameters-'+i+'-parameter_type-btn-1').show();
        } else if (parameter_type == 'quniform') {
            $('#create_study_parameters-'+i+'-parameter_type-btn-2').show();
        } else if (parameter_type == 'normal') {
            $('#create_study_parameters-'+i+'-parameter_type-btn-3').show();
        } else if (parameter_type == 'qnormal') {
            $('#create_study_parameters-'+i+'-parameter_type-btn-4').show();
        } else {
            $('#create_study_parameters-'+i+'-parameter_type-btn-1').show();
            console.log('Warning. Unknown parameter type in line: ', i);
        }

        /* Update placeholders */
        $('#create_study_parameters-'+i+'-parameter_range_a').show()
        $('#create_study_parameters-'+i+'-parameter_range_b').show()
        if (parameter_type == 'randint') {
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].value = 0;
            $('#create_study_parameters-'+i+'-parameter_range_a').hide();
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'Number of Categories';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d*';
        } else if (parameter_type == 'uniform' || parameter_type == 'loguniform') {
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].placeholder = 'From';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'To';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].pattern = '\d.\d*';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d.\d*';
        } else if (parameter_type == 'quniform' || parameter_type == 'qloguniform') {
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].placeholder = 'From';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'To';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].step = '1';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = '1';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].pattern = '\d*';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d*';
        } else if (parameter_type == 'normal' || parameter_type == 'lognormal') {
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].placeholder = 'Mean';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'Std';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].pattern = '\d.\d*';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d.\d*';
        } else if (parameter_type == 'qnormal' || parameter_type == 'qlognormal') {
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].placeholder = 'Mean';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'Std';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].step = '1';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = '1';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].pattern = '\d*';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d*';
        } else {
            console.log('[WARNING] Unknown parameter_type:')
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].placeholder = 'From?';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].placeholder = 'To?';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].step = 'any';
            $('#create_study_parameters-'+i+'-parameter_range_a')[0].pattern = '\d.\d*';
            $('#create_study_parameters-'+i+'-parameter_range_b')[0].pattern = '\d.\d*';
        }
    }
}

/**
 * Adjust the indices of form fields when removing items.
 */
function adjustIndices(removedIndex) {
    var $forms = $('.subform');

    $forms.each(function(i) {
        var $form = $(this);
        var index = parseInt($form.data('index'));
        var newIndex = index - 1;

        if (index < removedIndex) {
            // Skip
            return true;
        }

        // Change ID in form itself
        $form.attr('id', $form.attr('id').replace(index, newIndex));
        $form.data('index', newIndex);


        $form.find('div').each(function(idx) {
            var $item = $(this);

            if (this.hasAttribute('id')) {
                $item.attr('id', $item.attr('id').replace(index, newIndex));
            }
            if (this.hasAttribute('aria-labbelled-by')) {
                $item.attr('aria-labelled-by', $item.attr('id').replace(index, newIndex));
            }
        });
        $form.find('button').each(function(idx) {
            var $item = $(this);

            if (this.hasAttribute('id')) {
                $item.attr('id', $item.attr('id').replace(index, newIndex));
            }
            if (this.hasAttribute('href')) {
                $item.attr('href', $item.attr('href').replace(index, newIndex));
            }
        });
        $form.find('input').each(function(idx) {
            var $item = $(this);

            if (this.hasAttribute('id')) {
                $item.attr('id', $item.attr('id').replace(index, newIndex));
            }
            if (this.hasAttribute('name')) {
                $item.attr('name', $item.attr('name').replace(index, newIndex));
            }
        });
        $form.find('a').each(function(idx) {
            var $item = $(this);

            if (this.hasAttribute('id')) {
                $item.attr('id', $item.attr('id').replace(index, newIndex));
            }
            if (this.hasAttribute('href')) {
                $item.attr('href', $item.attr('href').replace(index, newIndex));
            }
        });

    });
}

/**
 * Remove a subform.
 */
function removeForm() {
    var $removedForm = $(this).closest('.subform');
    var removedIndex = parseInt($removedForm.data('index'));

    $removedForm.remove();

    // Update indices
    adjustIndices(removedIndex);
}

function onlyCharacters(event) {
    var k = event ? event.which : window.event.keyCode;
    var inp = String.fromCharCode(k);

    var warning = "";
    if (inp == ' ') {
        warning = "Try using a dash (-) instead of a space.";
        document.getElementById("only-characters-warning").innerHTML = warning;
        $('#only-characters-warning').show();

        return false;
    }
    if (!/[a-zA-Z0-9-_]/.test(inp)) {
        warning = "Study name can only contain characters, numbers and dashes.";
        document.getElementById("only-characters-warning").innerHTML = warning;
        $('#only-characters-warning').show();
        return false;
    }

    $('#only-characters-warning').hide();
}

/**
 * Add a new subform.
 */
function addForm() {
    var $templateForm = $('#parameter-PLACEHOLDER-form');

    if (!$templateForm) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index
    var $lastForm = $('.subform').last();

    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex > 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', $newForm.attr('id').replace('PLACEHOLDER', newIndex));
    $newForm.attr('data-index', $newForm.attr('data-index').replace('PLACEHOLDER', newIndex));
    $newForm.data('index', newIndex);


    $newForm.find('div').each(function(idx) {
        var $item = $(this);

        if (this.hasAttribute('id')) {
            $item.attr('id', $item.attr('id').replace('PLACEHOLDER', newIndex));
        }
        if (this.hasAttribute('aria-labbelled-by')) {
            $item.attr('aria-labelled-by', $item.attr('id').replace('PLACEHOLDER', newIndex));
        }
    });
    $newForm.find('button').each(function(idx) {
        var $item = $(this);

        if (this.hasAttribute('id')) {
            $item.attr('id', $item.attr('id').replace('PLACEHOLDER', newIndex));
        }
        if (this.hasAttribute('href')) {
            $item.attr('href', $item.attr('href').replace('PLACEHOLDER', newIndex));
        }
    });
    $newForm.find('input').each(function(idx) {
        var $item = $(this);

        if (this.hasAttribute('id')) {
            $item.attr('id', $item.attr('id').replace('PLACEHOLDER', newIndex));
        }
        if (this.hasAttribute('name')) {
            $item.attr('name', $item.attr('name').replace('PLACEHOLDER', newIndex));
        }
        this.required = true
    });
    $newForm.find('a').each(function(idx) {
        var $item = $(this);

        if (this.hasAttribute('id')) {
            $item.attr('id', $item.attr('id').replace('PLACEHOLDER', newIndex));
        }
        if (this.hasAttribute('href')) {
            $item.attr('href', $item.attr('href').replace('PLACEHOLDER', newIndex));
        }
    });

    // Append
    $('#subforms-container').append($newForm);
    $newForm.addClass('subform');
    $newForm.removeClass('is-hidden');

    $newForm.find('.remove').click(removeForm);

}

function selectParameterType(study_index, parameter_index) {
    var n_types = 5;
    for(var i=0; i<n_types; i++) {
      if (i == parameter_index) {
        $('#create_study_parameters-'+study_index+'-parameter_type-'+i)[0].checked = true;
      } else {
        $('#create_study_parameters-'+study_index+'-parameter_type-'+i)[0].checked = false;
      }
    }
    $('#modal-parameter_type-'+study_index).modal('hide');

    updateCreateStudyForm();
}

$(document).ready(function() {

    if ($('#create-form').exists()) {
        // Update range fields
        $('form').change(updateCreateStudyForm);
        $('form').click(updateCreateStudyForm);

        // Add new row
        $('#add-row').click(addForm);
        $('#add-row').click(updateCreateStudyForm);

        // Remove a row
        $('.remove').click(removeForm);

        // Advanced checker
        $('#advancedButton').click(function() {
            $('.is_advanced').show();
            $('#easyButton').show();
            $('#advancedButton').hide();
        });
        $('#easyButton').click(function() {
            $('.is_advanced').hide();
            $('#easyButton').hide();
            $('#advancedButton').show();
        });


        // Update form
        updateCreateStudyForm();
    }

    // Clickable rows in table
    $('tr[data-href]').click(function(e) {
        if($(event.target).is("a") || $(event.target).is("button") || $(event.target).is(".dropdown")) {
            // $($(event.target).data('target')).modal('show');
            // e.stopPropagation();
            // e.preventDefault();
        } else {
            document.location = $(this).data('href');
        }
    });
});


// Map [Enter] key to work like the [Tab] key
// Daniel P. Clark 2014

// Catch the keydown for the entire document
$(document).keydown(function(e) {

  // Set self as the current item in focus
  var self = $(':focus'),
      // Set the form by the current item in focus
      form = self.parents('form:eq(0)'),
      focusable;

  // Array of Indexable/Tab-able items
  focusable = form.find('input,a,select,button,textarea,div[contenteditable=true]').filter(':visible');

  function enterKey(){
    if (e.which === 13 && !self.is('textarea,div[contenteditable=true]')) { // [Enter] key

      // If not a regular hyperlink/button/textarea
      if ($.inArray(self, focusable) && (!self.is('a,button,input'))){
        // Then prevent the default [Enter] key behaviour from submitting the form
        e.preventDefault();
      } // Otherwise follow the link/button as by design, or put new line in textarea

      // Focus on the next item (either previous or next depending on shift)
      focusable.eq(focusable.index(self) + (e.shiftKey ? -1 : 1)).focus();

      return false;
    }
  }
  // We need to capture the [Shift] key and check the [Enter] key either way.
  if (e.shiftKey) { enterKey() } else { enterKey() }
});

