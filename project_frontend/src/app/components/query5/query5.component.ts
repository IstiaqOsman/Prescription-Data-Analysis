import {Component, OnInit} from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";
import {ChartDataset, ChartOptions} from "chart.js";


@Component({
  selector: 'app-query5',
  templateUrl: './query5.component.html',
  styleUrls: ['./query5.component.css']
})

export class Query5Component implements OnInit {


  data_all: any[] = [];
  service: any[] = [];
  count: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "doughnut",
      label: 'Visit count',
      data: this.count,
    }
  ];



  chartLabels: string[] = this.service;
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // // ⤵️ Remove the grids
    // scales: {
    //   xAxis: {
    //     display: false,
    //     grid: {
    //       drawBorder: false // removes random border at bottom
    //     }
    //   },
    //   yAxis: {
    //     display: false
    //   }
    // },

    plugins: {

      legend: {
        display: true
      },




      tooltip: {
        // ⤵️ tooltip main styles
        backgroundColor: '#ffeaff',
        displayColors: false, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#0b4ad2',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#2D2F33',
        bodyFont: {
          size: 13
        }
      }
    }
  };

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query5Data();
  }

  query5Data(): void {
    this.queryService.getQuery5().subscribe((data: any) => {
        console.log(data)
        for (const d of data) {
          this.service.push(d.Service_Name)
          this.count.push(d.Count)
        }
        this.data_all = data;
      }
    )
  }

}
