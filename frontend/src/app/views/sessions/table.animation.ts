import { trigger, sequence, stagger, animate, transition, style, query, animateChild } from '@angular/animations';

export const rowAnimation =
    trigger('rowAnimation', [
        transition(':enter', [
            style({ opacity: 0 }),
            animate('.05s ease-in',
                style({ opacity: 1 }))
        ])
    ])

export const tableAnimation =
    trigger('tableAnimation', [
        transition(':enter', [
            query('@rowAnimation', stagger(15, animateChild()))
        ])
    ])