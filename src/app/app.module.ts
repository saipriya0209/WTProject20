import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatDialogModule} from '@angular/material/dialog';
import {MatTableModule} from '@angular/material/table';
import {MatGridListModule} from '@angular/material/grid-list';
<<<<<<< HEAD
=======

>>>>>>> f4f60c3593a01b048defffe744f5124189a8317e

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { Routes, RouterModule } from '@angular/router';
import { AppRoutingModule } from './router-module.module';
import { ProfileComponent } from './profile/profile.component';
import { StudentService } from './student.service';
import { OrganiserService } from './organiser.service';
import { CreateEvent } from './organiser/create_event/create_event.component';
import { AllEvents } from './organiser/list_event/list_event.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {DialogOverviewExampleDialog} from './organiser/allocate_funds/allocate_funds.component';
import {ExpenseLog} from './organiser/expense_log/expense_log.component';
import { PrizeDistb } from './organiser/prize_dist/prize_dist.component';
import { DisplayRegistrationTable } from './organiser/display_reg/display_reg.component';
<<<<<<< HEAD
import { OrganiserStatistics } from './organiser/organiser_statistics/organiser_statistics.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatRadioModule } from '@angular/material/radio';
import {MatButtonModule} from '@angular/material/button';

=======
>>>>>>> f4f60c3593a01b048defffe744f5124189a8317e


const routes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'newevent', component: CreateEvent },
  {path: 'allevents', component: AllEvents},
  {path: 'statistics', component: OrganiserStatistics}
]

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    ProfileComponent,
    CreateEvent,
    AllEvents,
    DialogOverviewExampleDialog,
    ExpenseLog,
    PrizeDistb,
<<<<<<< HEAD
    DisplayRegistrationTable,
    OrganiserStatistics
=======
    DisplayRegistrationTable
>>>>>>> f4f60c3593a01b048defffe744f5124189a8317e
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatDialogModule,
    MatTableModule,
    MatGridListModule,
<<<<<<< HEAD
    MatInputModule,
    MatFormFieldModule,
    MatRadioModule,
    MatButtonModule
=======

>>>>>>> f4f60c3593a01b048defffe744f5124189a8317e
  ],
  providers: [StudentService, OrganiserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
