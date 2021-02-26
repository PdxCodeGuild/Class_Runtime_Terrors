var chart = new CanvasJS.Chart("chartContainer2", {
    title:{
        text: "My First Chart in CanvasJS"              
    },
    data: [              
    {
        // Change type to "doughnut", "line", "splineArea", etc.
        type: "splineArea",
        dataPoints: [
            { label: "apple",  y: 10  },
            { label: "orange", y: 15  },
            { label: "banana", y: 25  },
            { label: "mango",  y: 30  },
            { label: "grape",  y: 28  }
        ]
    }
    ]
});
chart.render();