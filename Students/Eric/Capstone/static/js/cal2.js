//Un needed

//Learn about axios
// axios({
//   method: 'get',
//   url: 'http://127.0.0.1:8000/core/get_events'
// }).then(reponse => {
//   console.log(reponse.data)
// }) 
// axios({
//   method: 'get',
//   url: '{% url "core:get_events" %}'
// }).then(reponse => {
//   console.log(reponse.data)
// }) 


// document.addEventListener('DOMContentLoaded', function() {
//   var calendarEl = document.getElementById('calendar');

//   var calendar = new FullCalendar.Calendar(calendarEl, {
//     initialView: 'dayGridMonth',
//     initialDate: '2021-02-07',
//     headerToolbar: {
//       left: 'prev,next today',
//       center: 'title',
//       right: 'dayGridMonth,timeGridWeek,timeGridDay'
//     },
//     events: [
//       {
//         title: 'All Day Event',
//         start: '2021-02-11'
//       },
//       {
//         title: 'Long Event',
//         start: '2021-02-07',
//         end: '2021-02-10'
//       },
//       {
//         groupId: '999',
//         title: 'Repeating Event',
//         start: '2021-02-09T16:00:00'
//       },
//       {
//         groupId: '999',
//         title: 'Repeating Event',
//         start: '2021-02-16 11:00:00'
//       },
//       {
//         title: 'Conference',
//         start: '2021-02-11',
//         end: '2021-02-13'
//       },
//       {
//         title: 'Meeting',
//         start: '2021-02-12T10:30:00',
//         end: '2021-02-12T12:30:00'
//       },
//       {
//         title: 'Lunch',
//         start: '2021-02-12T12:00:00'
//       },
//       {
//         title: 'Meeting',
//         start: '2021-02-12T14:30:00'
//       },
//       {
//         title: 'Birthday Party',
//         start: '2021-02-13T07:00:00'
//       },
//       {
//         title: 'Click for Google',
//         url: 'http://google.com/',
//         start: '2021-02-28'
//       }
//     ]
//   });

//   calendar.render();
// });