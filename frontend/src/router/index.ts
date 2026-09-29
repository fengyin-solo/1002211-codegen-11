import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Extinguisher = () => import('@/views/extinguisher/index.vue')
const Hydrant = () => import('@/views/hydrant/index.vue')
const Alarmhost = () => import('@/views/alarmhost/index.vue')
const Detector = () => import('@/views/detector/index.vue')
const Pumphouse = () => import('@/views/pumphouse/index.vue')
const Watertank = () => import('@/views/watertank/index.vue')
const Door = () => import('@/views/door/index.vue')
const Shutter = () => import('@/views/shutter/index.vue')
const Exit = () => import('@/views/exit/index.vue')
const Sprinkler = () => import('@/views/sprinkler/index.vue')
const Gas = () => import('@/views/gas/index.vue')
const Drill = () => import('@/views/drill/index.vue')
const Training = () => import('@/views/training/index.vue')
const Change = () => import('@/views/change/index.vue')
const Fault = () => import('@/views/fault/index.vue')
const Cert = () => import('@/views/cert/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/extinguisher', name: 'extinguisher', component: Extinguisher },
    { path: '/hydrant', name: 'hydrant', component: Hydrant },
    { path: '/alarmhost', name: 'alarmhost', component: Alarmhost },
    { path: '/detector', name: 'detector', component: Detector },
    { path: '/pumphouse', name: 'pumphouse', component: Pumphouse },
    { path: '/watertank', name: 'watertank', component: Watertank },
    { path: '/door', name: 'door', component: Door },
    { path: '/shutter', name: 'shutter', component: Shutter },
    { path: '/exit', name: 'exit', component: Exit },
    { path: '/sprinkler', name: 'sprinkler', component: Sprinkler },
    { path: '/gas', name: 'gas', component: Gas },
    { path: '/drill', name: 'drill', component: Drill },
    { path: '/training', name: 'training', component: Training },
    { path: '/change', name: 'change', component: Change },
    { path: '/fault', name: 'fault', component: Fault },
    { path: '/cert', name: 'cert', component: Cert },
  ],
})

export default router
