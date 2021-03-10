<script type='text/javascript' src="{{ url_for('static', filename='jquery.js') }}"></script>
<script type='text/javascript'>
  $SCRIPT_ROOT = '{{ request.script_root|tojson|safe }}';
</script>
<script type="text/javascript">
  $(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });
</script>
<h1>jQuery Example</h1>
<p><input type="text" size="5" name="a"> +
   <input type="text" size="5" name="b"> =
   <span id="result">?</span></p>
<p><a href="#" id="calculate">calculate server side</a></p>