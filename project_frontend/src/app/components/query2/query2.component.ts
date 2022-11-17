import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query2',
  templateUrl: './query2.component.html',
  styleUrls: ['./query2.component.css']
})
export class Query2Component implements OnInit {

  data_all: any[] = [];
  ingredients_data: any[]  = [];
  sales_data: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "polarArea",
      label: 'Sales',
      data: this.sales_data
    }
  ];
  chartLabels: string[] = this.ingredients_data;
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
    this.Query2Data();
  }

  Query2Data(): void{
    this.queryService.getQuery2().subscribe((data:any)=>{
      console.log(data);
      for(const d of data){
        //console.log(d.Sales, d.Type)
        this.ingredients_data.push(d.Ingredient_Appliance)
        this.sales_data.push(d.Total_Sales)
      }
      this.data_all = data;
    }
    )
  }

}
