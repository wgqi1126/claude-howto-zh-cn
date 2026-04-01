# 重构目录

精选自 Martin Fowler《重构》（第 2 版）的重构技法。每项重构均包含动机、分步做法与示例。

> 「重构是由其做法定义的——为完成改动而遵循的精确步骤序列。」—— Martin Fowler

---

## 如何使用本目录

1. 借助代码坏味道参考**识别坏味道**
2. 在本目录中**找到对应的重构**
3. **按步骤逐一执行**做法
4. **每步之后运行测试**，确保行为不变

**黄金法则**：若任一步超过 10 分钟，请拆成更小的步骤。

---

## 最常见的重构

### 提炼函数（Extract Method）

**适用情形**：函数过长、重复代码、需要为一段逻辑命名

**动机**：把一段代码变成函数，用名称表达其用途。

**做法**：
1. 新建一个函数，按「做什么」命名（而非「怎么做」）
2. 将代码片段复制到新函数中
3. 扫描片段中用到的局部变量
4. 将局部变量作为参数传入（或在函数内声明）
5. 妥善处理返回值
6. 用对新函数的调用替换原片段
7. 测试

**重构前**：
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // 计算未付金额
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // 打印明细
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**重构后**：
```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### 内联函数（Inline Method）

**适用情形**：函数体与其名称一样直白、过度委托

**动机**：在函数并未增加价值时，去掉多余的间接层。

**做法**：
1. 确认该函数不是多态的
2. 找出对该函数的所有调用
3. 将每次调用替换为函数体
4. 每次替换后测试
5. 删除函数定义

**重构前**：
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**重构后**：
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### 提炼变量（Extract Variable）

**适用情形**：复杂表达式难以理解

**动机**：为复杂表达式的一部分命名。

**做法**：
1. 确认表达式无副作用
2. 声明一个不可变变量
3. 将其设为该表达式（或其中一部分）的结果
4. 用变量替换原表达式
5. 测试

**重构前**：
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**重构后**：
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### 内联变量（Inline Variable）

**适用情形**：变量名没有比表达式传递更多信息

**动机**：去掉不必要的间接层。

**做法**：
1. 确认右侧无副作用
2. 若变量可变，先改为不可变并测试
3. 找到第一次引用处，替换为表达式
4. 测试
5. 对其余引用重复
6. 删除声明与赋值
7. 测试

---

### 变量改名（Rename Variable）

**适用情形**：名称未能清楚表达用途

**动机**：好名字对整洁代码至关重要。

**做法**：
1. 若变量使用面很广，考虑先封装
2. 找出所有引用
3. 逐一修改引用
4. 测试

**提示**：
- 使用能表达意图的名称
- 避免缩写
- 使用领域术语

```javascript
// 不好
const d = 30;
const x = users.filter(u => u.a);

// 好
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### 改变函数声明（Change Function Declaration）

**适用情形**：函数名未说明用途，或需要调整参数

**动机**：好的函数名使代码自解释。

**做法（简单）**：
1. 删除不需要的参数
2. 修改名称
3. 添加需要的参数
4. 测试

**做法（迁移——用于复杂变更）**：
1. 若要删除参数，确认已不再使用
2. 按目标签名新建函数
3. 让旧函数调用新函数
4. 测试
5. 将调用方改为使用新函数
6. 每处修改后测试
7. 删除旧函数

**重构前**：
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**重构后**：
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### 封装变量（Encapsulate Variable）

**适用情形**：多处直接访问同一数据

**动机**：为数据操作提供明确的入口。

**做法**：
1. 创建 getter 与 setter 函数
2. 找出所有引用
3. 读操作改为走 getter
4. 写操作改为走 setter
5. 每次修改后测试
6. 收紧变量的可见范围

**重构前**：
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// 多处使用
spaceship.owner = defaultOwner;
```

**重构后**：
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### 引入参数对象（Introduce Parameter Object）

**适用情形**：多个参数经常成组出现

**动机**：把天然属于一组的数据聚在一起。

**做法**：
1. 为成组参数新建类/结构
2. 测试
3. 用「改变函数声明」加入新对象参数
4. 测试
5. 对组内每个参数，从函数签名中移除并改用新对象
6. 每步后测试

**重构前**：
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**重构后**：
```javascript
class DateRange {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
}

function amountInvoiced(dateRange) { ... }
function amountReceived(dateRange) { ... }
function amountOverdue(dateRange) { ... }
```

---

### 将函数组合成类（Combine Functions into Class）

**适用情形**：多个函数操作同一批数据

**动机**：把函数与它们操作的数据放在一起。

**做法**：
1. 对公共数据使用「封装记录」（Encapsulate Record）
2. 将每个函数移入类
3. 每次移动后测试
4. 用类字段替代原先的数据参数

**重构前**：
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**重构后**：
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### 拆分阶段（Split Phase）

**适用情形**：一段代码同时处理两件不同的事

**动机**：拆成阶段清晰、边界分明的代码。

**做法**：
1. 为第二阶段再写一个函数
2. 测试
3. 在两阶段之间引入中间数据结构
4. 测试
5. 将第一阶段提炼为独立函数
6. 测试

**重构前**：
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  const shippingPerCase = (basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = quantity * shippingPerCase;
  return basePrice - discount + shippingCost;
}
```

**重构后**：
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const priceData = calculatePricingData(product, quantity);
  return applyShipping(priceData, shippingMethod);
}

function calculatePricingData(product, quantity) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  return { basePrice, quantity, discount };
}

function applyShipping(priceData, shippingMethod) {
  const shippingPerCase = (priceData.basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = priceData.quantity * shippingPerCase;
  return priceData.basePrice - priceData.discount + shippingCost;
}
```

---

## 搬移特性

### 搬移函数（Move Method）

**适用情形**：函数更多使用另一个类的特性，而非自身所在类

**动机**：把函数放到最常一起使用的数据旁。

**做法**：
1. 检查该函数在所属类中用到的所有程序元素
2. 确认函数是否多态
3. 将函数复制到目标类
4. 按新上下文调整
5. 让原函数委托给目标
6. 测试
7. 考虑删除原函数

---

### 搬移字段（Move Field）

**适用情形**：字段更多被另一个类使用

**动机**：数据跟着使用它的函数走。

**做法**：
1. 若尚未封装，先封装该字段
2. 测试
3. 在目标类中创建字段
4. 更新引用以使用目标字段
5. 测试
6. 删除原字段

---

### 将语句搬移到函数（Move Statements into Function）

**适用情形**：某段代码总是与一次函数调用一起出现

**动机**：把重复出现的语句移入函数，消除重复。

**做法**：
1. 若尚未提炼，先把重复代码提炼成函数
2. 将语句移入该函数
3. 测试
4. 若调用方不再需要独立语句，则删除

---

### 将语句搬移到调用方（Move Statements to Callers）

**适用情形**：共同行为在各调用方之间不同

**动机**：当行为需要因调用方而异时，把它移出函数。

**做法**：
1. 对要搬移的代码使用「提炼函数」
2. 对原函数使用「内联函数」
3. 删除已内联的调用
4. 将提炼出的代码分别放到各调用方
5. 测试

---

## 组织数据

### 以对象取代基本类型（Replace Primitive with Object）

**适用情形**：数据项需要比简单值更多的行为

**动机**：把数据与其行为封装在一起。

**做法**：
1. 使用「封装变量」
2. 创建一个简单的值对象类
3. 修改 setter，创建新实例
4. 修改 getter，返回内部值
5. 测试
6. 在新类上添加更丰富行为

**重构前**：
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // 字符串："high"、"rush" 等
  }
}

// 用法
if (order.priority === "high" || order.priority === "rush") { ... }
```

**重构后**：
```javascript
class Priority {
  constructor(value) {
    if (!Priority.legalValues().includes(value))
      throw new Error(`Invalid priority: ${value}`);
    this._value = value;
  }

  static legalValues() { return ['low', 'normal', 'high', 'rush']; }
  get value() { return this._value; }

  higherThan(other) {
    return Priority.legalValues().indexOf(this._value) >
           Priority.legalValues().indexOf(other._value);
  }
}

// 用法
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### 以查询取代临时变量（Replace Temp with Query）

**适用情形**：临时变量保存某表达式的结果

**动机**：把表达式提炼成函数，使代码更清晰。

**做法**：
1. 确认变量只被赋值一次
2. 将赋值右侧提炼为方法
3. 用方法调用替换对临时变量的引用
4. 测试
5. 删除临时变量的声明与赋值

**重构前**：
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**重构后**：
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// 在方法内
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## 简化条件逻辑

### 分解条件表达式（Decompose Conditional）

**适用情形**：复杂的条件（if-then-else）语句

**动机**：通过提炼条件与分支动作，使意图清晰。

**做法**：
1. 对条件使用「提炼函数」
2. 对 then 分支使用「提炼函数」
3. 对 else 分支（若有）使用「提炼函数」

**重构前**：
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**重构后**：
```javascript
if (isSummer(aDate, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = regularCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function regularCharge(quantity, plan) {
  return quantity * plan.regularRate + plan.regularServiceCharge;
}
```

---

### 合并条件表达式（Consolidate Conditional Expression）

**适用情形**：多个条件得到相同结果

**动机**：表明这些条件属于同一次检查。

**做法**：
1. 确认条件中无副作用
2. 用 `and` 或 `or` 合并条件
3. 可对合并后的条件考虑「提炼函数」

**重构前**：
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**重构后**：
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### 以卫语句取代嵌套条件（Replace Nested Conditional with Guard Clauses）

**适用情形**：嵌套过深，流程难读

**动机**：对特例使用卫语句并提前返回，让主流程保持平直。

**做法**：
1. 找出特例条件
2. 改为卫语句并提前 return
3. 每次修改后测试

**重构前**：
```javascript
function payAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reasonCode: "SEP" };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reasonCode: "RET" };
    } else {
      result = calculateNormalPay(employee);
    }
  }
  return result;
}
```

**重构后**：
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### 以多态取代条件表达式（Replace Conditional with Polymorphism）

**适用情形**：按类型的 switch/case，或随类型变化的条件逻辑

**动机**：让对象各自处理自己的行为。

**做法**：
1. 建立类层次（若尚不存在）
2. 用工厂函数创建对象
3. 将条件逻辑移到父类方法
4. 为每种情况在子类中实现方法
5. 删除原条件分支

**重构前**：
```javascript
function plumages(birds) {
  return birds.map(b => plumage(b));
}

function plumage(bird) {
  switch (bird.type) {
    case 'EuropeanSwallow':
      return "average";
    case 'AfricanSwallow':
      return (bird.numberOfCoconuts > 2) ? "tired" : "average";
    case 'NorwegianBlueParrot':
      return (bird.voltage > 100) ? "scorched" : "beautiful";
    default:
      return "unknown";
  }
}
```

**重构后**：
```javascript
class Bird {
  get plumage() { return "unknown"; }
}

class EuropeanSwallow extends Bird {
  get plumage() { return "average"; }
}

class AfricanSwallow extends Bird {
  get plumage() {
    return (this.numberOfCoconuts > 2) ? "tired" : "average";
  }
}

class NorwegianBlueParrot extends Bird {
  get plumage() {
    return (this.voltage > 100) ? "scorched" : "beautiful";
  }
}

function createBird(data) {
  switch (data.type) {
    case 'EuropeanSwallow': return new EuropeanSwallow(data);
    case 'AfricanSwallow': return new AfricanSwallow(data);
    case 'NorwegianBlueParrot': return new NorwegianBlueParrot(data);
    default: return new Bird(data);
  }
}
```

---

### 引入特例（空对象）（Introduce Special Case (Null Object)）

**适用情形**：对特例反复做 null 检查

**动机**：返回能处理该特例的专用对象。

**做法**：
1. 创建具备预期接口的特例类
2. 添加 isSpecialCase 检查
3. 引入工厂方法
4. 用特例对象用法替换 null 检查
5. 测试

**重构前**：
```javascript
const customer = site.customer;
// …… 多处检查
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**重构后**：
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// 工厂方法
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// 用法：无需再做空值检查
const customerName = customer.name;
```

---

## 重构 API

### 将查询函数和修改函数分离（Separate Query from Modifier）

**适用情形**：函数既返回值又有副作用

**动机**：明确哪些操作有副作用。

**做法**：
1. 新建查询函数
2. 复制原函数的返回逻辑
3. 将原函数改为无返回值（void）
4. 替换依赖返回值的调用
5. 测试

**重构前**：
```javascript
function alertForMiscreant(people) {
  for (const p of people) {
    if (p === "Don") {
      setOffAlarms();
      return "Don";
    }
    if (p === "John") {
      setOffAlarms();
      return "John";
    }
  }
  return "";
}
```

**重构后**：
```javascript
function findMiscreant(people) {
  for (const p of people) {
    if (p === "Don") return "Don";
    if (p === "John") return "John";
  }
  return "";
}

function alertForMiscreant(people) {
  if (findMiscreant(people) !== "") setOffAlarms();
}
```

---

### 函数参数化（Parameterize Function）

**适用情形**：多个函数做类似的事，仅字面量不同

**动机**：通过增加参数消除重复。

**做法**：
1. 选定一个函数
2. 为变化的那部分字面量增加参数
3. 修改函数体使用参数
4. 测试
5. 将调用方改为使用参数化版本
6. 删除不再使用的函数

**重构前**：
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**重构后**：
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// 用法
raise(person, 0.10);
raise(person, 0.05);
```

---

### 移除标记参数（Remove Flag Argument）

**适用情形**：布尔参数改变函数行为

**动机**：用独立函数让行为显式化。

**做法**：
1. 为每个标记取值建立显式函数
2. 将每次调用改为对应的新函数
3. 每次修改后测试
4. 删除原函数

**重构前**：
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // 高端预订逻辑
  } else {
    // 普通预订逻辑
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**重构后**：
```javascript
function bookPremiumConcert(customer) {
  // 高端预订逻辑
}

function bookRegularConcert(customer) {
  // 普通预订逻辑
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## 与继承打交道

### 函数上移（Pull Up Method）

**适用情形**：多个子类中有相同方法

**动机**：消除类层次中的重复。

**做法**：
1. 检查各方法是否实质相同
2. 确认签名一致
3. 在父类中新建方法
4. 从某一子类复制方法体
5. 删除一个子类方法并测试
6. 逐个删除其余子类方法并测试

---

### 函数下移（Push Down Method）

**适用情形**：行为仅与部分子类相关

**动机**：把方法放在真正需要它的地方。

**做法**：
1. 将方法复制到每个需要的子类
2. 从父类删除该方法
3. 测试
4. 从不需要的子类中删除
5. 测试

---

### 以委托取代子类（Replace Subclass with Delegate）

**适用情形**：继承使用不当，需要更大灵活性

**动机**：在合适时优先组合而非继承。

**做法**：
1. 创建空的委托类
2. 在宿主类中增加持有委托的字段
3. 为委托编写构造函数，由宿主调用
4. 将特性移到委托
5. 每次移动后测试
6. 用委托替换继承

---

## 提炼类（Extract Class）

**适用情形**：大类承担多种职责

**动机**：拆分类以维持单一职责。

**做法**：
1. 确定如何划分职责
2. 新建类
3. 将字段从原类移到新类
4. 测试
5. 将方法从原类移到新类
6. 每次移动后测试
7. 审视并为两个类改名
8. 决定如何对外暴露新类

**重构前**：
```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**重构后**：
```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## 速查：坏味道与重构

| 代码坏味道 | 首选重构 | 备选 |
|------------|-------------------|-------------|
| 过长函数（Long Method） | 提炼函数 | 以查询取代临时变量 |
| 重复代码（Duplicate Code） | 提炼函数 | 函数上移 |
| 过大的类（Large Class） | 提炼类 | 提炼子类 |
| 过长参数列（Long Parameter List） | 引入参数对象 | 保持对象完整 |
| 依恋情结（Feature Envy） | 搬移函数 | 提炼函数 + 搬移 |
| 数据泥团（Data Clumps） | 提炼类 | 引入参数对象 |
| 基本类型偏执（Primitive Obsession） | 以对象取代基本类型 | 以类取代类型码 |
| switch 语句（Switch Statements） | 以多态取代条件表达式 | 以类取代类型码 |
| 临时字段（Temporary Field） | 提炼类 | 引入空对象 |
| 消息链（Message Chains） | 隐藏委托关系 | 提炼函数 |
| 中间人（Middle Man） | 移除中间人 | 内联函数 |
| 发散式变化（Divergent Change） | 提炼类 | 拆分阶段 |
| 霰弹式修改（Shotgun Surgery） | 搬移函数 | 内联类 |
| 死代码（Dead Code） | 移除死代码 | - |
| 夸夸其谈通用性（Speculative Generality） | 折叠继承体系 | 内联类 |

---

## 延伸阅读

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code*（第 2 版）
- 在线目录：https://refactoring.com/catalog/
