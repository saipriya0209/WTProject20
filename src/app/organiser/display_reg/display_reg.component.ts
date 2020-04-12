import {Component, Inject} from '@angular/core';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { HttpClient } from '@angular/common/http';
import {MatTableModule} from '@angular/material/table';

@Component({
  selector: 'display_reg',
  templateUrl: 'display_reg.component.html',
  styleUrls: ['display_reg.component.css']
})

export class DisplayRegistrationTable {
  serverData: object;
  displayedColumns: object;
  rows: Array<object>;
  rid: Array<number>;
  sid: Array<number>;

  constructor(public dialogRef: MatDialogRef<DisplayRegistrationTable>, private httpClient: HttpClient, @Inject(MAT_DIALOG_DATA) public data2: any) {
    this.displayedColumns = ['registration_id', 'student_id'];
  }

  ngOnInit() {

    this.httpClient.post('http://127.0.0.1:5000/show_reg', {'e_id': this.data2.event[0]}).toPromise().then(data => {
        this.serverData = data as JSON;
        console.log(this.serverData["data"]);
        var data1 = []
        var amount1 = []
        for(var x in this.serverData["data"]) {
          data1.push(this.serverData["data"][x][0]);
          amount1.push(this.serverData["data"][x][1]);
        }
        this.rid = data1;
        this.sid = amount1;
        this.random();
    });
  }

  random() {
    this.rows = [];
    for(var x = 0; x < this.rid.length; x++) {
      this.rows.push({});
      this.rows[x] = ({"r_id": this.rid[x], "s_id":this.sid[x]});
    }
    console.log(this.rows);
  }

  onClick() {
    this.dialogRef.close();
  }

}

