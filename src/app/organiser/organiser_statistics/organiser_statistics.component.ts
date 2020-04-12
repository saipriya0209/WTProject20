import {Component} from '@angular/core';
import { OrganiserService } from 'src/app/organiser.service';
import { HttpClient } from '@angular/common/http';
import * as CanvasJS from './canvasjs.min';

@Component({
  selector: 'org-statistics',
  templateUrl: 'organiser_statistics.component.html'
})

export class OrganiserStatistics {
  message: object;
  serverData: object;
  constructor(private data1: OrganiserService, private httpClient: HttpClient) {
  }

  ngOnInit() {
    this.data1.currentMessage.subscribe((message) => this.message = message);
    console.log(this.data1.currentMessage);
    this.httpClient.post('http://127.0.0.1:5000/totalprofit', {'o_id': this.message['o_id']}).subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);

      let chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        exportEnabled: true,
        title: {
          text: "Profit made per event"
        },
        data: [{
          type: "column",
          dataPoints: this.serverData
        }]
      });
      chart.render();
  });
}
}
