$(document).ready(function() {
  $.getJSON('schedule.json', function(data) {
    fillSchedule(data)
  })
});

function fillSchedule(data) {

  var thead = document.createElement("thead")
  
  var th_date = document.createElement("th")
  th_date.setAttribute("scope", "col")
  th_date.innerHTML = "Date"
  thead.appendChild(th_date)

  var th_topic = document.createElement("th")
  th_topic.setAttribute("scope", "col")
  th_topic.innerHTML = "Topic"
  thead.appendChild(th_topic)

  var th_handout = document.createElement("th")
  th_handout.setAttribute("scope", "col")
  th_handout.innerHTML = "Lecture notes"
  thead.appendChild(th_handout)
  
  var th_asg = document.createElement("th")
  th_asg.setAttribute("scope", "col")
  th_asg.innerHTML = "Assignment"
  thead.appendChild(th_asg)
  
  document.getElementById("scheduleTable").appendChild(thead)

  var tbody = document.createElement("tbody")

  var highlight_first = false
  for (var i in data.schedule) {
    var day = data.schedule[i]
    var date = new Date(day.date)
    var now = new Date()
    var type = day.type
  
    var row = document.createElement("tr")

    if (now > date) {
      row.setAttribute("class", "table-success")
    }
    else if (now <= date && !highlight_first) {
      row.setAttribute("class", "table-warning")
      highlight_first = true
    }
    else if (type == "Lab") {
      row.setAttribute("class", "table-primary")
    }
    else if (type == "NoClass") {
      row.setAttribute("class", "table-active")
    }
    else if (type == "Exam") {
      row.setAttribute("class", "table-danger")
    }
    else if (type == "AsgnDue") {
      row.setAttribute("class", "table-info")
    }

    // Date
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    var m = months[date.getMonth()] 
    var d = date.getDate()
    if (d < 10) {d = "0" + d}
    var td = document.createElement("td")
    td.innerHTML = m + " " + d
    row.appendChild(td)

    // Topic
    var topic = day.topic
    var td = document.createElement("td")
    td.innerHTML = topic
    row.appendChild(td)

    // Handout
    var notes = day.notes
    var code = day.code
    var slides = day.slides
    var td = document.createElement("td")
    var notes_link = ""
    if (notes != "") {
	notes_link = "<a href=\"" + notes + "\">[Technical notes]</a>"
    }
    var code_link = ""
    if (code != "") {
      code_link = "<a href=\"" + code + "\">[Notebook]</a>"
    }
    var slides_link = ""
    if (slides != "") {
      slides_link = "<a href=\"" + slides + "\">[Lecture PDF]</a>"
    }
    var content = ""
    if (code_link != "" && notes_link != "" && slides_link != "") {
      content = code_link + ", " + slides_link + ", " + notes_link
    }
    else if (code_link != "" && notes_link != "") {
      content = code_link + ", " + notes_link
    }
    else if (slides_link != "" && notes_link != "") {
      content = slides_link + ", " + notes_link
    }
    else if (slides_link != "") {
      content = slides_link
    }
    else {
      content = code_link + notes_link
    }
    td.innerHTML = content
    row.appendChild(td)
    
    // Homework
    var hw = day.hw
    var td = document.createElement("td")
    td.innerHTML = hw
    row.appendChild(td)
  
    tbody.appendChild(row)
  }
  document.getElementById("scheduleTable").appendChild(tbody)

}
