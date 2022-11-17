import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all: any[] = [];
  items: any[] = [];
  quarter: any[] = [];

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit(): void {
    this.Query8Data();
  }

  Query8Data(): void{
    this.queryService.getQuery8().subscribe((data:any)=>{
        console.log(data);
        for(const d of data){
          //console.log(d.Sales, d.Type)
          this.items.push(d.Item)
          this.quarter.push(d.Quarter)
        }
        this.data_all = data;
      }
    )
  }

}
