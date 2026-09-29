<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">消防设施维保管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向灭火器、消火栓、报警主机、消防泵房、防火分隔、疏散通道与消防演练的一体化消防设施维保管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "灭火器管理", path: "/extinguisher" }, { label: "消火栓管理", path: "/hydrant" }, { label: "报警主机管理", path: "/alarmhost" }, { label: "探测器管理", path: "/detector" }, { label: "消防泵房管理", path: "/pumphouse" }, { label: "消防水池管理", path: "/watertank" }, { label: "防火门管理", path: "/door" }, { label: "防火卷帘管理", path: "/shutter" }, { label: "疏散通道管理", path: "/exit" }, { label: "喷淋系统管理", path: "/sprinkler" }, { label: "气体灭火系统", path: "/gas" }, { label: "消防演练管理", path: "/drill" }, { label: "消防培训管理", path: "/training" }, { label: "动火审批", path: "/change" }, { label: "故障报修", path: "/fault" }, { label: "消防许可证件管理", path: "/cert" }]
</script>
