import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProfileComponent } from './profile/profile.component';
import { CreateEvent } from './organiser/create_event/create_event.component';
import { AllEvents } from './organiser/list_event/list_event.component';
import { OrganiserStatistics } from './organiser/organiser_statistics/organiser_statistics.component';

const appRoutes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'newevent', component: CreateEvent},
  {path: 'allevents', component: AllEvents},
  {path: 'statistics', component: OrganiserStatistics}

]

@NgModule({
    imports: [
        RouterModule.forRoot(appRoutes)
    ],
    exports: [
        RouterModule
    ]
})
export class AppRoutingModule {}
