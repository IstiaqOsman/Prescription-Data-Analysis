import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query3',
  templateUrl: './query3.component.html',
  styleUrls: ['./query3.component.css']
})
export class Query3Component implements OnInit {

  data_all: any[] = [];
  pco: any[] = [];
  sales: any[] = [];


  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Sales in Taka',
      data: this.sales,
    }
  ];
  chartLabels: string[] = this.pco;
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

  constructor(private queryService: QueryService, private http: HttpClient) { }

  ngOnInit(): void {
    this.getQuery3Data();
  }
  getQuery3Data(): void {
    this.queryService.getQuery3().subscribe((data:any)=> {
      console.log(data);
      for (const d of data) {
        //console.log(d.District, d.Sales)

        this.pco.push(d.PCO)
        this.sales.push(d.Total_Sales)
      }
      this.data_all = data;
    })
  }

}
