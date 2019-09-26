#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-scala-reflect
Version  : 1
Release  : 3
URL      : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.jar
Source0  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.jar
Source1  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.jar
Source2  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.pom
Source3  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.pom
Source4  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.jar
Source5  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.pom
Source6  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.jar
Source7  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.pom
Source8  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.jar
Source9  : https://repo.maven.apache.org/maven2/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-scala-reflect-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-scala-reflect package.
Group: Data

%description data
data components for the mvn-scala-reflect package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.jar
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.3/scala-reflect-2.10.3.pom
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.jar
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.10.6/scala-reflect-2.10.6.pom
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.jar
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.11.12/scala-reflect-2.11.12.pom
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.jar
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.7/scala-reflect-2.12.7.pom
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.jar
/usr/share/java/.m2/repository/org/scala-lang/scala-reflect/2.12.8/scala-reflect-2.12.8.pom
