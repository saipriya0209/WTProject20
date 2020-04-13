import { Component, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { StudentService } from './student.service';
import { ProfileComponent } from './profile/profile.component';
import {OrganiserService} from './organiser.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css', '../../node_modules/materialize-css/dist/css/materialize.min.css']
})

export class AppComponent {
  title = 'app';
  message: object;
  serverData: JSON;
  message1: object;

  constructor(private httpClient: HttpClient, private organiser: OrganiserService, private student: StudentService) {
    this.organiser.currentMessage.subscribe(message => {this.message = message; console.log(this.message); });
    this.student.currentMessage.subscribe(message1 => {this.message = message1; console.log(this.message); });
  }

  ngOnInit() {
    this.message = {}
    this.message1 = {}
  }

  show() {
    //console.log(this.student.currentMessage);
    if('first_name' in this.message && 'o_id' in this.message) {
      return true;
    }
    else
      return false;
  }

  setempty() {
    this.organiser.changeMessage({});
    //console.log(this.student.currentMessage);
    this.show();
  }

  show1() {
    if('first_name' in this.message && 's_id' in this.message) {
      return true;
    }
    else
      return false;
  }
}
