import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatDialogModule} from '@angular/material/dialog';
import {MatTableModule} from '@angular/material/table';
import {MatGridListModule} from '@angular/material/grid-list';
import {DialogOverviewExampleDialog} from './organiser/allocate_funds/allocate_funds.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatRadioModule } from '@angular/material/radio';
import {MatButtonModule} from '@angular/material/button';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


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
import {ExpenseLog} from './organiser/expense_log/expense_log.component';
import { PrizeDistb } from './organiser/prize_dist/prize_dist.component';
import { DisplayRegistrationTable } from './organiser/display_reg/display_reg.component';
import { OrganiserStatistics } from './organiser/organiser_statistics/organiser_statistics.component';
import { ShomeComponent } from './shome/shome.component';
import { DispEvents } from './student/list_event/list_event.component';
import { RegEvent } from './student/reg_event/reg_event.component';
import { GetTeam } from './student/get_team/get_team.component';
import { DispPrizes } from './student/list_prize/list_prize.component';
import { EventDet } from './student/event_details/event_details.component';
import { DispOrg } from './student/display_org/display_org.component';
import { TeamInput } from './student/team_input/team_input.component';
import { AfterReg } from './student/after_reg/after_reg.component';



const routes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'newevent', component: CreateEvent },
  {path: 'allevents', component: AllEvents},
  {path: 'statistics', component: OrganiserStatistics},
  {path: 'studentprofile', component: ShomeComponent},
  {path: 'dispevents', component: DispEvents},
  {path: 'regevent', component: RegEvent},
  {path:'getteam',component: GetTeam},
  {path: 'dispprizes', component: DispPrizes},
  {path:'eventdet',component: EventDet},
  {path:'disporg',component: DispOrg},
  {path:'teaminp',component: TeamInput},
  {path:'afterreg',component: AfterReg},
  {path: 'eventdet', component: EventDet},
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
    DisplayRegistrationTable,
    OrganiserStatistics,
    ShomeComponent,
    DispEvents,
    RegEvent,
    GetTeam,
    DispPrizes,
    EventDet,
    DispOrg,
    AfterReg,
    TeamInput
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
    MatInputModule,
    MatFormFieldModule,
    MatRadioModule,
    MatButtonModule
  ],
  providers: [StudentService, OrganiserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
