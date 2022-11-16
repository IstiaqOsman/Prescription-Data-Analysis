import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { QueriesService } from 'src/app/services/queries.service';
import {ChartDataset, ChartOptions} from 'chart.js';

@Component({
  selector: 'app-query1',
  templateUrl: './query1.component.html',
  styleUrls: ['./query1.component.css']
})
export class Query1Component implements OnInit {

  data_all:any[] = [];
  month:any[] = [];
  NIC:any[] = [];
  total_sales:any[] = [];


  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Net Ingredient Cost',
      data: this.NIC,
    },
    {
      type: "line",
      label: 'Total Sales in Taka',
      data: this.total_sales,
      pointBackgroundColor: 'black'
    },
    

  ];
  chartLabels: string[] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
    scales: {
      xAxis: {
        display: false,
        grid: {
          drawBorder: true // removes random border at bottom
        }
      },
      yAxis: {
        display: true
      }
    },

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


  constructor(private queryService: QueriesService, private http: HttpClient) { }

  ngOnInit(): void {
    this.query1Data();
  }
  query1Data(): void{
    this.queryService.getQuery1().subscribe((data:any)=>{
      console.log(data);
      for(const d of data){
        this.month.push(d.Month);
        this.NIC.push(d.NIC);
        this.total_sales.push(d.total_sales);
      }
      this.data_all = data;
    })
  }

}
