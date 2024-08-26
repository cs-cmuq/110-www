$(document).ready(function() {
  $.getJSON('schedule.json', function(data) {
    fillSchedule(data, "scheduleTable")
  })
});

function fillSchedule(data, tableID) {

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
  th_handout.innerHTML = "Files"
  thead.appendChild(th_handout)
  
  document.getElementById(tableID).appendChild(thead)

  var tbody = document.createElement("tbody")

  var highlight_first = false
  
  for (var i in data.schedule) {
    
    var day = data.schedule[i]
    var date = new Date(day.date)
    var now = new Date()
    var type = day.type
  
    var row = document.createElement("tr")
    if (day['beginWeek'])
    {
      row.setAttribute("style", "border-top: 2px solid black")
    }
    
    var cell_class = ""

    if (type == "Lecture") {
      cell_class = "table-light"
    }
    else if (type == "Lab") {
      cell_class = "table-success"
    }
    else if (type == "NoClass") {
      cell_class = "table-active"
    }
    else if (type == "Exam") {
      cell_class = "table-danger"
    }
    else if (type == "AsgnDue") {
      cell_class = "table-secondary"
    }

    // Date
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    var days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    var wd = days[date.getDay()]
    var m = months[date.getMonth()] 
    var d = date.getDate()
    if (d < 10) {d = "0" + d}
    var td = document.createElement("td")
    td.innerHTML = wd + " " + m + " " + d
    td.setAttribute("class", cell_class)
    row.appendChild(td)

    // Topic
    var topic = day.topic
    var td = document.createElement("td")
    if (now > date) {
      td.innerHTML = "<s>" + topic + "</s>"
    }
    else {
      td.innerHTML = topic
    }
    td.setAttribute("class", cell_class)
    row.appendChild(td)

    // Files
    var td = document.createElement("td")
    
    var notes_link = ""
    if (day['notes']) {
	notes_link = "<a href=\"" + day.notes + "\">Notes</a>"
    }
    
    var noteb_link = ""
    if (day['noteb']) {
      noteb_link = "<a href=\"" + day.noteb + "\">Notebook</a>"
    }
    
    var slides_link = ""
    if (day['slides']) {
      slides_link = "<a href=\"" + day.slides + "\">Slides</a>"
    }

    var hw_link = ""
    if (day['hw']) {
      parts = day.hw.split("/")
      link_name = parts[parts.length-1]
      hw_link = "<a href=\"" + day.hw + "\">" + link_name + "</a>"
    }
    
    var content = [notes_link, noteb_link, slides_link, hw_link].filter(function(link){return link != ""}).join(", ")
    td.innerHTML = content
    td.setAttribute("class", cell_class)
    row.appendChild(td)
    
    tbody.appendChild(row)
  }
  document.getElementById(tableID).appendChild(tbody)

}
