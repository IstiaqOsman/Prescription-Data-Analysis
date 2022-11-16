import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { QueriesService } from '../services/queries.service';
import { ChartDataset, ChartOptions } from 'chart.js';

@Component({
  selector: 'app-query2',
  templateUrl: './query2.component.html',
  styleUrls: ['./query2.component.css']
})
export class Query2Component implements OnInit {


  data_all:any[] = [];
  stp_name:any[] = [];
  count_of_pco:any[] = [];
  count_of_bnf:any[] = [];
  ratio:any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "line",
      label: 'Numbers of PCO per STP',
      data: this.count_of_pco,
      // pointBackgroundColor: 'black'
    },
    {
      type: "bar",
      label: 'Numbers of BNF per STP',
      data: this.count_of_bnf,
    },
    {
      type: "line",
      label: 'ratio between PCO and BNF',
      data: this.ratio,
    },

  ];
  chartLabels: string[] = this.stp_name

  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
    // scales: {
    //   xAxis: {
    //     display: false,
    //     grid: {
    //       drawBorder: true // removes random border at bottom
    //     }
    //   },
    //   yAxis: {
    //     display: true

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



  constructor(private queryService: QueriesService, private http: HttpClient) { }

  ngOnInit(): void {
    this.query2Data();
  }
  query2Data(): void{
    this.queryService.getQuery2().subscribe((data:any)=>{
      console.log(data);
      for(const d of data){
        this.stp_name.push(d.stp_name);
        this.count_of_bnf.push(d.count_of_bnf);
        this.count_of_pco.push(d.count_of_pco);
        this.ratio.push(d.count_of_bnf/d.count_of_pco);

      }
      this.data_all = data;
    })
  }
  

}
