import { Component, OnInit } from '@angular/core';

// Declare var tableau because it is referencing the tableau js library
declare var tableau: any;

@Component({
  selector: 'app-query11',
  templateUrl: './query11.component.html',
  styleUrls: ['./query11.component.css']
})
export class Query11Component{
  title = 'Tableau in Angular';
  // Declare an instance of viz
  viz: any;

  ngOnInit() {
    var placeholderDiv = document.getElementById('vizContainer');
    // Replace this url with the url of your Tableau dashboard
    var url = 'https://public.tableau.com/views/test_16680934243520/Sheet1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link';
    var options = {
      hideTabs: true,
      width: "80%",
      height: "500px",
      onFirstInteractive: function() {
        // The viz is now ready and can be safely used.
        console.log("Run this code when the viz has finished loading.");
      }
    };
    // Creating a viz object and embed it in the container div.
    this.viz = new tableau.Viz(placeholderDiv, url, options);
  }
}
