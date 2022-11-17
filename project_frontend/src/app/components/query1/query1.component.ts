import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query1',
  templateUrl: './query1.component.html',
  styleUrls: ['./query1.component.css']
})


export class Query1Component implements OnInit {



  data_all: any[] = [];
  ingredients: any[] = [];
  quantity: any[] = [];


  chartData: ChartDataset[] = [
    {

      type: "pie",
      label: 'Prescribed Quantity',
      data: this.quantity,
    },


  ];
  chartLabels: string[] = this.ingredients;

  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,


   /* animation: {
      onComplete: () => {


        delayed = true;
      },
      delay: (context) => {
        let delay = 0;
        if (context.type === 'data' && context.mode === 'default' && !delayed) {
          delay = context.dataIndex * 300 + context.datasetIndex * 100;
        }
        return delay;
      },
    },*/

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
        backgroundColor: '#433e3e',
        displayColors: false, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#d2a40b',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#fef3f3',
        bodyFont: {
          size: 13
        }

      }

    }

  };

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query1Data();
  }

  query1Data(): void {
    this.queryService.getQuery1().subscribe((data: any) => {
        for (const d of data) {
          this.ingredients.push(d.Ingredient_Appliance)
          this.quantity.push(d.Total_Quantity)
        }
        this.data_all = data;
      }
    )
  }

}
