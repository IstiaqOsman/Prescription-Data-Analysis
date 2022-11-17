import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query10',
  templateUrl: './query10.component.html',
  styleUrls: ['./query10.component.css']
})

export class Query10Component implements OnInit {
  data_all: any[] = [];
  store: any[] = [];
  month: any[] = [];
  avg_sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Sales in Taka',
      data: this.avg_sales
    }
  ];
  chartLabels: string[] = this.month;
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
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
    // }

    plugins: {
      legend: {
        display: true,
        labels: {
          color: 'rgb(14,38,3)'
        }
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

  ngOnInit(): void {
    this.Query10Data();
  }

  Query10Data(): void{
    this.queryService.getQuery10().subscribe((data:any)=>{
        console.log(data);
        for(const d of data){
          //console.log(d.Sales, d.Type)
          this.store.push(d.Store)
          this.month.push(d.Month)
          this.avg_sales.push(d.Average_Sales)
        }
        this.data_all = data;
      }
    )
  }

}
