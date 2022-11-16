import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = "http://127.0.0.1:5000/api"

@Injectable({
  providedIn: 'root'
})
export class QueriesService {

  constructor(private http: HttpClient) { }
  getQuery1(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q9`);
    
  }

  getQuery2(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q10`);
    
  }
  // getQuery7(days:any): Observable<any>{
  //   const httpOptions = {
  //     headers: new HttpHeaders(
  //     { 
  //       //  'Authorization': 'Your Token',
  //        'content-Type': 'application/json'
  //     })
  // }
  //   // const headers = {'content_type': 'application/json'}
  //   const body = JSON.stringify({'days':days});
  //   return this.http.post(`${baseUrl}/q7`, body, httpOptions);
    
  // }
  
}
